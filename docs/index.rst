.. SPDX-FileCopyrightText: 2022 Kari Argillander
..
.. SPDX-License-Identifier: CC0-1.0

.. toctree::
   :maxdepth: 2
   :hidden:

   deployment.rst
   contributing.rst
   license.rst

======
Sopaca
======

Sopaca aims to be tool which can calculate how cost efficiency solar panels are
based on various factors. Factors can be example

* System cost
* Maintenance cost
* System efficiency loss over time
* Real energy consumption data
* Real solar radiation data (based on location)
* Energy cost (seller/transfer)

Many other tools just say how long is payback time or how big system you should
get. In my opinion we should company these things to x and y axes. Maybe most
optimal system is 10kW system which payback time is 15.5 years. Ok cool but what
if 50kw system has payback time 16 years. Yes that is not optimal but if you
have money you can choose how much profit you want to get. Also payback time is
same thing as profit margin so we should really make that clear.

Many tools of course cost lot of money and I just wanted to make some open
source version. Of course I learn also lot of this.

Technical idea
==============

1. We get user electricity consumption report(s).

   User can upload electricity consumption report. We parse this with
   consumption_import. We can get lot of good info from this. Example we can get
   address which we can use to get target coordinates.

   We could also give user possibility to just select where consumption report
   is and our site will download this file. This will be lot of work, but it
   will be amazing user experience. Still have to think is this even legal thing
   to do because we need to ask credentials to another site and make robot to
   navigate that site. Some sites might have API for this so then this should
   probably be ok.

   If we cannot identify this file we should ask user permission to use this
   file for development to make site better.

2. We get radiation data from https://re.jrc.ec.europa.eu/

   At first we just use API for this. If this site get's popular we should
   probably store this data to us so we do not load their server too much.

3. Now we can already estimate payback times pretty well.

   This data is already pretty accurate without anymore tweaking. Tweaking can
   still benefit user to select right system. We can also estimate if user
   should wait for year before doing decision based on inflation and system
   cost/kWh over time.

4. User can still tweak parameters to get better estimate

Location
--------

Location info is really important to us as we can do lot of estimations based on
that. We try to get this info from user as subtly as possible. This way user
experience will be much better.

   1. We try to get address from electricity consumption report.
   2. We try to get location from user location data if it is enabled.
   3. We try to identify location from IP
   4. We can try identify language and base our guess to that.

We should have some location based on IP, but of course we have to have some
fail safe. Location can always be given by user from map.


Technical implementation
========================

We use

* Python to write this website.
* Django framework to do many things easier for us.
* Dash apps to display and manipulating data.
* Pandas to analyze and manipulate data.
* mysql/postgres to store data (Django handle these)

We store datasets for user if they ever wanna check calculations again. We might
also do better calculations and maybe user want to check those also. Or maybe
user want to check couple years later if now is the time to get solar panels.


Libraries needed to write:

1. Consumption import

   Idea is that user can give any csv or excel report and library will output
   data.

   Library should accept files or data so it will be flexible for other use
   cases also.

   This library should also make fake data to example fill missing months. Also
   we want to calculate electricity on minute based and many sites just give
   hour based data so we have to make algorithm to do that.

2. Solar radiation

   We need to make library which will get data from https://re.jrc.ec.europa.eu/
   because this is rate limited and we want to get data straight to Pandas. We
   could probably do this in app itself but I feel it is nice if this is library
   which can be used independently.

   Also in some point we can change this to our own implementation if we want. I
   do not yet know if *jrc* data is real or calculated. If it is just calculated
   we can maybe randomize this data a little bit so we get better real world
   example. Also we need to randomize data at minute level at least.

3. Location to electric company

   It would be nice to make library which tells based on location which
   electricity company is in this area. This info can be used to example extract
   prices straight from specific company. Or maybe give link and documentation
   to user how to download energy report.

   In Finland at least every electricity company has map which has boarders they
   own. It is easy to make collector which we can use map location to company.
   Here is example https://katkot.pks.fi/outages/outageReport/mobilemap

4. Payback chart calculators

   Main calculating library which will take lot of different Panda datasets and
   calculate payback times.


Future thinking
===============

Maybe we can also calculate how profitable is to used example Tesla power wall
kind of solutions. Also wind power should not be too hard after we have
components ready. Also calculating what which type of deal you should make with
electricity company should not be too difficult.

There is lot of good tools already which can benefit calculations. In my mind
these tools are too optimistic and estimate too many things. Also tweaking
possibilities are very minimal.

* https://sunroof.withgoogle.com/
* https://sunaurinkosahko.sunenergia.com/
* https://solar.so.energy/quote/intro/roof-drawing
* https://easysolar.app/en/
* https://thesolarlabs.com/
* https://www.thesolarnerd.com/calculator/
* https://www.mapdevelopers.com/area_finder.php
