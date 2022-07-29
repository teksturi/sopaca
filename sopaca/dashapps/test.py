# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash

app = DjangoDash("test")

app.layout = html.Div(
    [
        dcc.RadioItems(
            id="dropdown-color",
            options=[{"label": c, "value": c.lower()} for c in ["Red", "Blue"]],
            value="red",
        ),
        html.Div(id="output-color"),
    ]
)


@app.callback(
    dash.dependencies.Output("output-color", "children"),
    [dash.dependencies.Input("dropdown-color", "value")],
)
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value
