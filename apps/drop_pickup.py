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

# components
dropChoices = dcc.Checklist(
    options=[
        {
            "label": "I want the pet-sitter to come pick up my dog.",
            "value": "dropAtHome",
        },
        {"label": "I drop my dog at the pet-sitter's place.", "value": "dropAtSitters"},
    ],
    labelStyle=dict(display="block"),
    id="drop-choice",
)

pickupChoices = dcc.Checklist(
    options=[
        {
            "label": "I want the pet-sitter to come drop my dog.",
            "value": "pickupAtHome",
        },
        {
            "label": "I go pick up my dog at the sitter's place.",
            "value": "pickupAtSitters",
        },
    ],
    labelStyle=dict(display="block"),
    id="pickup-choice",
)

submitButton = html.A(
    html.Button("Submit", className="submit-button", id="submit-button", n_clicks=0),
    href="/apps/congrats",
)

layout = html.Div(
    [
        html.H3("Choose how you want to drop your dog"),
        html.Div(dropChoices),
        html.H3("Choose how you want to pick up your dog"),
        html.Div(pickupChoices),
        submitButton,
    ]
)


@app.callback(
    [Output("intermediate-value-3", "children")],
    [
        Input("drop-choice", "value"),
        Input("pickup-choice", "value"),
        Input("submit-button", "n_clicks"),
    ],
)
def submit_checklist1(
    dropChoice,
    pickupChoice,
    n_clicks,
):
    intermediate_value = {
        "dropChoice": dropChoice,
        "pickupChoice": pickupChoice,
    }
    print("intermediate_value is", intermediate_value)
    intermediate_value = json.dumps(intermediate_value)
    return intermediate_value