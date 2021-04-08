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
from app import app
import json

# read datasets
df_reviews = pd.read_csv("/Users/mmiyazaki/Documents/Coco/data/reviews.csv")
df = pd.read_csv("/Users/mmiyazaki/Documents/Coco/data/sample.csv")

# images
image_directory = "/Users/mmiyazaki/Documents/Coco/assets/pictures"

layout = html.Div([])


@app.callback(
    Output("finalcheck", "children"),
    [
        Input("sitters-page-url", "pathname"),
        Input("intermediate-value-2", "children"),
        Input("intermediate-value-3", "children"),
    ],
)
def display_finalCheckList(pathname, value2, value3):
    if pathname == "/apps/congrats":
        json_data2 = json.loads(value2)
        json_data3 = json.loads(value3)
        print(json_data2)
        print(json_data3)
        div = html.Div(json_data2)
        return div
    else:
        return html.Div([])
