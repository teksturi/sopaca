# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

"""
    This module contains consumption parsers.
"""

__PARSERS = []


def load():
    """
    Import all consumption parsers
    """

    from . import vattenfall as p1

    __PARSERS.append(p1.comsumption_parser)


def all():
    """
    Get a list of all loaded consumption parses
    """
    return __PARSERS
