.. SPDX-FileCopyrightText: 2022 Kari Argillander
..
.. SPDX-License-Identifier: CC0-1.0

========
Licenses
========

Source files are licensed with GPL-2.0-only. Documentation and configure files
are licensed with CC0-1.0. Note that probably configure files do not even be
copyrightable material but as we want every file containing license we use that.
Project use SPDX license headers. We use tool *Reuse* to make sure every file
have proper license.

If you use some copied code from another Open Source project please use right
license for that. Not every license is acceptable though.

You can add license text to new source files with::

   reuse addheader --copyright "$(git config --get user.name)" --license GPL-2.0-only src/example.py

Or for documentation and configure files::

   reuse addheader --copyright "$(git config --get user.name)" --license CC0-1.0 docs/example.py
