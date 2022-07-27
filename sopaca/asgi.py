# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

"""
ASGI config for Sopaca project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sopaca.settings")

application = get_asgi_application()
