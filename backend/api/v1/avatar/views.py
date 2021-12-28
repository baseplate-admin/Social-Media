from libravatar import libravatar_raw_query
from platform import python_version
from asgiref.sync import sync_to_async

# Django imports
from django.http.response import HttpResponse
from api.v1.avatar.services.database import increase_avatar_count_by_one

from custom.user.models import CustomUser

# PIL for image resizing
from PIL import Image
from io import BytesIO

# Monkeypatch
import pillow_avif

# Create your views here.


async def avatar(request, user_id) -> HttpResponse:
    # Save a statistics to DB
    await increase_avatar_count_by_one()
    # Get user | Note that our user model is custom
    user = await sync_to_async(CustomUser.objects.get, thread_sensitive=True)(
        id=user_id
    )

    email = user.email
    query = await libravatar_raw_query(email, dict(request.GET))
    result = await query
    # Remove link to remove tracking
    result.headers.pop("Link", None)

    # Remove the Content-Type and Content-Length
    result.headers.pop("Content-Type", None)
    result.headers.pop("Content-Length", None)

    # No reason. Just to be a bit more transparent
    result.headers["server"] = f"Python/{python_version()}"

    # Pillow processing
    res = Image.open(BytesIO(await result.aread()))
    in_memory = BytesIO()
    res.save(in_memory, format="avif")

    return HttpResponse(
        # await result.aread(),
        in_memory.getvalue(),
        content_type="image/avif",
        headers=result.headers,
    )
