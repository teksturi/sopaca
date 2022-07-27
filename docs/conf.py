# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import sys
from datetime import date

# Project info
project = "Sopaca"
author = "Kari Argillander"
copyright = f"{date.today().year}, Kari Argillander"

# Settings
master_doc = "index"
nitpicky = True

exclude_patterns = ["Thumbs.db", ".DS_Store", "_build/**"]

# Style
html_theme = "sphinx_rtd_theme"

# Extensions
extensions = [
    # Lot of cool little things
    "sphinx_design",
    # Code gets copy button in html
    "sphinx_copybutton",
]

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

    spelling_lang = "en_US"
    spelling_warning = True
