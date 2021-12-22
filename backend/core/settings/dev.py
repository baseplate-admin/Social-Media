from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mn19l@e%r^s&a^pa9%(bf173v-0c54^@3s(pb!ts_yuts0$+6p"

ALLOWED_HOSTS = [
    "127.0.0.1",
]

# # Causes error with async stuff
# INSTALLED_APPS += [
#     "debug_toolbar",
# ]
# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

INTERNAL_IPS = ALLOWED_HOSTS

DEBUG = True
