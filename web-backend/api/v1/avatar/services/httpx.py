from typing import Dict
from hashlib import md5

import httpx
from httpx._models import Response


async def httpx_get_avatar(
    avatar_url: str,
    email: str,
    params: Dict[str, int] = {
        "s": 3840,
    },
) -> Response:
    client = httpx.AsyncClient(http2=True)

    result: Response = await client.get(
        f"{avatar_url}/avatar/{md5(email.lower().encode()).hexdigest()}",
        params=params,
    )

    print(f"HTTPX fetching avatar for : {str(email)}")
    print(f"HTTPX getting image from : {str(result.url)}")

    return result
