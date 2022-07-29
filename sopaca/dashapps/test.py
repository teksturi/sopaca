# SPDX-FileCopyrightText: 2022 Kari Argillander
#
# SPDX-License-Identifier: GPL-2.0-only

import pandas as pd
import plotly.graph_objs as go
from dash import Input, Output, State, dcc, exceptions, html
from django_plotly_dash import DjangoDash
from geopy.geocoders import Nominatim

app = DjangoDash("test")

# Location picker


def location_picker():
    return html.Div(
        [
            html.H1(children="Location finder"),
            dcc.Input(
                id="location-input",
                placeholder="Address or location",
                type="text",
            ),
            html.Button(id="find-location", children="Find"),
            html.Div(id="location-output"),
            html.Div(id="location-latitude"),
            html.Div(id="location-longitude"),
        ]
    )


def get_location(address):
    # TODO: For production this should also contain email. Maybe we can just
    # use Django admin email. Also user_agent should come from settings.
    geolocator = Nominatim(user_agent="sopaca")
    location = geolocator.geocode(address)

    return location.latitude, location.longitude, location.address


@app.callback(
    Output("location-latitude", "children"),
    Output("location-longitude", "children"),
    Output("location-output", "children"),
    Input("find-location", "n_clicks"),
    State("location-input", "value"),
    prevent_initial_call=True,
)
def update_latitude_longitude(n_clicks, value):
    if not value:
        raise exceptions.PreventUpdate
    return get_location(value)


# System cost


def system_cost_graph():
    cost = [[500, 3000], [1500, 5000], [3000, 8000], [15000, 20000]]
    df = pd.DataFrame(cost, columns=["peakpower", "cost"])

    graph = go.Scatter(
        x=df["peakpower"] / 1000,
        y=df["cost"],
        mode="lines",
        name="Estimated system cost",
        marker_color="blue",
        line_shape="spline",
    )
    layout = go.Layout(
        title="System cost",
        xaxis_ticksuffix="kWh",
        xaxis_tickformat=".1f",
        yaxis_ticksuffix="€",
        yaxis_tickformat=",.",
    )

    return {"data": [graph], "layout": layout}


# Layout


app.layout = html.Div(
    [
        location_picker(),
        html.Hr(),
        dcc.Graph(id="system-cost-graph", animate=True, figure=system_cost_graph()),
    ]
)
