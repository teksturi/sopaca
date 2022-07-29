# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: CC0-1.0

"""
Development settings for patchwork project.
These are also used in unit tests.

Desing based on https://github.com/getpatchwork/patchwork/blob/main/patchwork/settings/dev.py
"""

from .base import *  # noqa

SECRET_KEY = "django-insecure-oe&z&d3%*7p#%a@cx5(sp)+@(w8dk3w1r6pg7pu_$6ej80wg-b"
DEBUG = True
ALLOWED_HOSTS = []

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Use a faster, though less secure, password hasher for faster tests
# https://docs.djangoproject.com/en/2.2/topics/testing/overview/#password-hashing
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
