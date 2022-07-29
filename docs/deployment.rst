.. SPDX-FileCopyrightText: 2022 Kari Argillander
..
.. SPDX-License-Identifier: CC0-1.0

==========
Deployment
==========

This will help you when you want to run this website in production use. If you
just want to develop then you probably do not need this instruction. This is
also not full tutorial how to deploy Django app. This is just small notebook
which might help to deploy this app.

At least following environment variables should be set

``DJANGO_SETTINGS_MODULE``
   Default: *sopaca.settings.prod*.

   You should also probably check this file if you want to change some other
   settings which cannot be changed with environment variables.

``DJANGO_SECRET_KEY``
   Mandatory. You can generate new password with::

      openssl rand -base64 32

``DATABASE_PASSWORD``
   Default: ""

``DATABASE_TYPE``
   Select postgres or mysql

``DATABASE_HOST``
   Default: localhost

``DATABASE_PORT``
   Default: ""

``DATABASE_NAME``
   Default: sopaca

``DATABASE_USER``
   Default: sopaca

``EMAIL_HOST``
   Default: localhost

``EMAIL_PORT``
   Default: 25

``EMAIL_HOST_USER``
   Default: ""

``EMAIL_HOST_PASSWORD``
   Default: ""

``DEFAULT_FROM_EMAIL``
   Default: sopaca <sopaca@sopaca.example.com>

``ADMIN_EMAIL``
   Default: $DEFAULT_FROM_EMAIL

``ADMIN_NAME``
   Default: sopaca

``STATIC_ROOT``
   Default: ""

   Do we need any?
