from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    AVATAR_CHOICES = [
        ("https://seccdn.libravatar.org", "Libravatar"),
        ("https://www.gravatar.com", "Gravatar"),
    ]

    avatar_url = models.URLField(
        max_length=50,
        default="https://seccdn.libravatar.org",
        choices=AVATAR_CHOICES,
    )
