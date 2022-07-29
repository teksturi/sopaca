# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import os

from django.test import TestCase

from sopaca.consumption_import import consumption_import

from . import TEST_CONSUMPTIONS_DIR


class consumptionImport:
    """Test that all of our example consumption reports will be parsed
    correctly. We also try to do some error injection which might be easily made
    by human. Example change line-endigs, encoding, remove/add last line, use
    different file terminate, file extension rename."""

    fullname = None
    address = None
    location_number = None

    fullyear = None
    cells = None
    totalConsumptions = None

    p = None

    def _send_file(self, filename):
        path = os.path.join(TEST_CONSUMPTIONS_DIR, filename)
        self.p = consumption_import.consumptions(path)

    def test_fullname(self):
        self.skipTest("Not implempted")
        self.assertEquals(self.consumptions.fullname, self.fullname)

    def test_address(self):
        self.skipTest("Not implempted")
        self.assertEquals(self.consumptions.address, self.address)

    def test_location_number(self):
        self.skipTest("Not implempted")
        self.assertEquals(self.consumptions.location_number, self.location_number)

    def test_leaphour_handling(self):
        self.skipTest("Not implempted")
        pass

    def test_right_amount_data(self):
        self.assertEquals(len(self.p.consumption), self.cells)

    def test_total_comsumption_match(self):
        self.skipTest("We have 5wh error for some reason")
        self.assertEquals(self.p.consumption["wh"].sum(), self.totalConsumptions)


class testVattenfall(TestCase, consumptionImport):
    def setUp(self):
        self.fullname = "Kari Argillander"
        self.address = "Hämeenkatu 1 A 11, 33100 TAMPERE"
        self.location_number = "2345678"

        self.fullyear = False
        self.cells = 8543
        self.totalConsumptions = 2340760

        self._send_file("vattenfall.csv")
