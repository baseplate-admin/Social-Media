"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path, PurePath

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
REDIS: bool = True


# Custom login
# https://docs.djangoproject.com/en/4.0/topics/auth/default/
LOGIN_URL = "/authentication/login/"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Whitenoise patching
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # Custom stuff
    "custom.user",
    "custom.statistics",
    # Channels
    "channels",
    # API
    "api.v1.chats",
    "api.v1.avatar",
    # Pages
    "pages.home",
    "pages.authentication",
    "pages.users",
]

# https://docs.djangoproject.com/en/3.2/ref/middleware/#middleware-ordering

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # 1
    # Whitenoise
    "django.middleware.cache.UpdateCacheMiddleware",  # 2
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # 4
    "django.middleware.http.ConditionalGetMiddleware",  # 5
    "django.middleware.common.CommonMiddleware",  # 7
    "django.middleware.csrf.CsrfViewMiddleware",  # 8
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # 9
    "django.contrib.messages.middleware.MessageMiddleware",  # 10
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Request Middleware
    "core.middlewares.request.RequestMiddleware",
    # Strip whitespace
    # "strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom user model
# https://testdriven.io/blog/django-custom-user-model/

AUTH_USER_MODEL = "user.CustomUser"

# Password hashers
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    PurePath(BASE_DIR, "static"),
]

STATIC_ROOT = PurePath(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = PurePath(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Channels layers
# https://channels.readthedocs.io/en/stable/topics/channel_layers.html

if REDIS:
    try:
        # Failsafe
        import channels_redis

        CHANNEL_LAYERS = {
            "default": {
                "BACKEND": "channels_redis.core.RedisChannelLayer",
                "CONFIG": {
                    "hosts": [("127.0.0.1", 6379)],
                },
            },
        }

    except ImportError:
        CHANNEL_LAYERS = {
            "default": {
                "BACKEND": "channels.layers.InMemoryChannelLayer",
            }
        }


# Cache system
# https://docs.djangoproject.com/en/4.0/topics/cache/#redis

if REDIS:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "TIMEOUT": 5000,
        }
    }

else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique-snowflake",
            "TIMEOUT": 5000,
        }
    }
