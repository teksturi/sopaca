# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

from django.shortcuts import render


def home(request):
    return render(request, "home.html")
