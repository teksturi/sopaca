# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: CC0-1.0

import os

from .base import *  # noqa

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_PORT = os.getenv("EMAIL_PORT", 25)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL", "sopaca <sopaca@sopaca.example.com>"
)
SERVER_EMAIL = DEFAULT_FROM_EMAIL
NOTIFICATION_FROM_EMAIL = DEFAULT_FROM_EMAIL

admin_name = os.getenv("ADMIN_NAME", "sopaca")
admin_email = os.getenv("ADMIN_EMAIL", DEFAULT_FROM_EMAIL)
ADMINS = (
    # Add administrator contact details in the form:
    (admin_name, admin_email),
)

#
# Static files settings
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-files
# https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
#
STATIC_ROOT = os.environ.get("STATIC_ROOT", "")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
