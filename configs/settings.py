"""
Django settings for API AUTH project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

APP_NAME = "ALPHA ARCHIVE"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4^^prl9x#qe*0gu2!_r_v7$*kx83$)i2^9a*7qw%86^t0#z)go"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "generic",
    "user",
    "authentication",
    "tag",
    "file",
    "image_text",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "authentication.authentication.CustomTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "EXCEPTION_HANDLER": "generic.exceptions.custom_exception_handler",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "generic.pagination.CustomLimitOffsetPagination",
    "PAGE_SIZE": 100,
}

AUTHENTICATION_BACKENDS = [
    "authentication.backends.AuthentificationBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "alpha_archives",
        "USER": "root",
        "PASSWORD": "pwd",
        "HOST": "db",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
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

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# User model for authentication process

AUTH_USER_MODEL = "user.CustomUser"

# Email config for sending confirmation mail and more

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.develmail.com"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_VALIDATION_URL = "http://localhost:3000/email-confirmation/"
PASSWORD_RESET_URL = "http://localhost:3000/password-reset/"

if not EMAIL_HOST_PASSWORD or not EMAIL_HOST_USER:
    print(
        "SMTP NOT CONFIGURED : Please fill EMAIL_HOST_PASSWORD & EMAIL_HOST_USER located in main/settings.py"
    )

# Media config for images

MEDIA_HOST_URL = "http://localhost:8000"
MEDIA_URL = "media/"
INCOMING_URL = "incoming/"
INCOMING_ROOT = str(BASE_DIR) + "/" + MEDIA_URL + INCOMING_URL
MEDIA_ROOT = str(BASE_DIR) + "/" + MEDIA_URL

IMAGE_THUMBNAIL_WIDTH = 200  # px for auto generated thumbnail (generic img, see utils/database_builder config for modify screenshot thumbnail)
IMAGE_MAX_WIDTH = 1200  # px for all incoming images
IMAGE_COMPRESSION_LEVEL = 60  # % for all incoming images

# CORS

CORS_ORIGIN_ALLOW_ALL = (
    True  # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
)
CORS_ALLOW_CREDENTIALS = False


# Upload

DISABLE_UPLOAD = False
DISABLE_UPLOAD_SERVER_HDD_SPACE_LEFT = 5  # gb

# Input

FORBIDDEN_CHAR = ".?/!%*µ$^)'(#\&@+²,;:<>}`+°¨{=[]|ø¹^" + '"'

# OCR endpoint

ACTIVATE_OCR_ENDPOINT = True
OCR_TOKEN = "9x3l2jHJfJ0efSzk3lf4zhaA"  # special token only used for saving OCR results