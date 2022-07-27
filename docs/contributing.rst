.. SPDX-FileCopyrightText: 2022 Kari Argillander
..
.. SPDX-License-Identifier: CC0-1.0

============
Contributing
============

This project try to use common and good open source habits. We also try to
automate much of never endings tasks like updating versions, code formatting,
license additions etc.

Virtual environment
-------------------

I have now choose to use *venv*. You can start venv::

   python3 -m venv .venv
   source .venv/bin/activate

GIT
---

Branch *main* is meant to be latest development version.

Pre-commit
----------
We use pre-commit hooks. Configure file is called *.pre-commit-config.yaml*. You
can use these hooks with::

   pre-commit install

EditorConfig
------------



Code formatting
---------------

This project use Black, Flake8 and isort. Running these can be done with Tox::

   tox -p

IDEs
----

Main IDE which we support is VSCode. We should always have environment when new
developer opens VSCode and install recommend packages.

For editors we have also file *.editorconfig* so editors can little bit easier
pick standards which we want to use.

Tox
---

requirements.txt
----------------

This file should be generated with *pipreqs*.
