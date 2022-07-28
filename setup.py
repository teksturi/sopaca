# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

from setuptools import setup

setup(
    name="Sopaca",
    version="0.0.1",
    author="Kari Argillander",
    description="Website for calculating solar panel savings.",
    python_requires=">=3.8, <4",
    install_requires=[
        "django",
        "pandas",
        "plotly",
    ],
    extras_require={
        "dev": [
            "pre-commit",
            "pipreqs",
            "tox",
        ],
    },
    package_data={
        "sample": [
            "example_data.csv",
        ],
    },
    entry_points={
        "runners": [
            "sample=sample:main",
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django :: 4.0",
        "Operating System :: OS Independent",
    ],
)
