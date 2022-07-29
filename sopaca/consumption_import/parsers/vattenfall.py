# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import pandas as pd


class comsumption_parser:
    """Parse Vattfall energy consumtion csv"""

    @staticmethod
    def identify(filename) -> bool:
        """Return true if parser thinks it can parse this file."""

        # Just very quick and dirty check for now
        try:
            df = pd.read_csv(filename, skiprows=4, sep=";", encoding="utf-16le")
            df = df.rename(columns={"Alkaen": "datetime_start"}, errors="raise")
            df = df.rename(columns={"Saakka": "datetime_end"}, errors="raise")
            df = df.rename(columns={"Kulutus (kWh)": "wh"}, errors="raise")
        except UnicodeDecodeError:
            return False
        except KeyError:
            return False

        return True

    def parse(filename):
        df = pd.read_csv(filename, skiprows=4, sep=";", encoding="utf-16le")

        df = df.rename(columns={"Alkaen": "datetime_start"}, errors="raise")
        df = df.rename(columns={"Saakka": "datetime_end"}, errors="raise")
        df = df.rename(columns={"Kulutus (kWh)": "wh"}, errors="raise")

        df = df[["datetime_start", "datetime_end", "wh"]]
        df["wh"] = df["wh"].apply(lambda x: int(x * 1000)).astype(int)

        return df
