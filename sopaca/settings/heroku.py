# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: CC0-1.0

from pathlib import Path

import django_heroku

from .prod import *  # noqa

BASE_DIR = Path(__file__).resolve().parent.parent.parent

django_heroku.settings(locals())

ALLOWED_HOSTS = [".herokuapp.com"]
CSRF_TRUSTED_ORIGINS = ["https://*.herokuapp.com"]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
