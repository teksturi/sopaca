# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only


class comsumption_parser:
    """Parse Vattfall energy consumtion csv"""

    @staticmethod
    def identify(filename) -> bool:
        """Return true if parser thinks it can parse this file."""

        return True

    def __init__(self):
        self.name = "Matti"
