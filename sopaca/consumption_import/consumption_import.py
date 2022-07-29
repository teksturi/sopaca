# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import pandas as pd

from . import parsers

parsers.load()


class consumptions:
    """This class try to parse consumption report. It will automatically try to
    identify and parse content."""

    __matches = []

    def __init__(self, filename):
        self.fullname = None
        self.address = None
        self.location_number = None

        self.consumption = pd.DataFrame()

        self.__find_parser_matches(filename)

        for p in self.__matches:
            print("Parser", p, "found match.")

        if len(self.__matches) > 0:
            self.consumption = p.parse(filename)

    def __find_parser_matches(self, filename):
        for parser in parsers.all():
            if parser.identify(filename):
                self.__matches.append(parser)

    def _parse(self):
        raise NotImplementedError


if __name__ == "__main__":
    p = consumptions("vattenfall.csv")
    print(p.fullname)
