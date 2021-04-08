from app import app
from app import server
from apps import home, pet_sitters, checklist, drop_pickup, congrats

import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy
import base64
import os
from os import listdir
from os.path import isfile, join
import random
from datetime import date
from datetime import datetime as dt

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                dcc.Link("Home", href="/apps/home"),
                # dcc.Link('Pet sitters', href='/apps/pet-sitters'),
                html.Div(id="intermediate-value", style={"display": "none"}),
                html.Div(id="intermediate-value-2", style={"display": "none"}),
                html.Div(id="intermediate-value-3", style={"display": "none"}),
            ],
            className="row",
        ),
        html.Div(id="page-content", children=[]),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/apps/home":
        return home.layout
    elif pathname == "/apps/pet-sitters":
        return pet_sitters.layout
    elif pathname == "/apps/checklist":
        return checklist.layout
    elif pathname == "/apps/drop_pickup":
        return drop_pickup.layout
    elif pathname == "/apps/congrats":
        return congrats.layout
    else:
        return home.layout


if __name__ == "__main__":
    app.run_server(
        debug=True,
        # host = '127.0.0.1',
        host="0.0.0.0",
        port=8080,
    )