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
foodCheckList = dcc.Checklist(
    options=[
        {"label": "I bring my own food!", "value": "food"},
    ],
    labelStyle=dict(display="block"),
)

foodComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his food?",
)

foodTimeCheckList = dcc.Checklist(
    options=[
        {"label": "6AM-8AM", "value": "6_8"},
        {"label": "8AM-10AM", "value": "8_10"},
        {"label": "10AM-12PM", "value": "10_12"},
        {"label": "12PM-2PM", "value": "12_14"},
        {"label": "2PM-4PM", "value": "14_16"},
        {"label": "4PM-6PM", "value": "16_18"},
        {"label": "6PM-8PM", "value": "18_20"},
        {"label": "8PM-10PM", "value": "20_22"},
        {"label": "10PM-12PM", "value": "22_0"},
    ],
    labelStyle=dict(display="block"),
)

snackCheckList = dcc.Checklist(
    options=[
        {"label": "I bring my own snacks!", "value": "snacks"},
    ],
    labelStyle=dict(display="block"),
)

snackComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his snacks?",
)

amenityCheckList = dcc.Checklist(
    options=[
        {"label": "I bring my own toys!", "value": "toys"},
        {"label": "I bring my own leash!", "value": "leash"},
        {"label": "I bring my own toilette sheets!", "value": "sheets"},
        {"label": "I bring my own blankets/bed!", "value": "bed"},
    ],
    labelStyle=dict(display="block"),
)

amenityComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his ammenities?",
)

walkTimeCheckList = dcc.Checklist(
    options=[
        {"label": "6AM-8AM", "value": "6_8"},
        {"label": "8AM-10AM", "value": "8_10"},
        {"label": "10AM-12PM", "value": "10_12"},
        {"label": "12PM-2PM", "value": "12_14"},
        {"label": "2PM-4PM", "value": "14_16"},
        {"label": "4PM-6PM", "value": "16_18"},
        {"label": "6PM-8PM", "value": "18_20"},
        {"label": "8PM-10PM", "value": "20_22"},
        {"label": "10PM-12PM", "value": "22_0"},
    ],
    labelStyle=dict(display="block"),
)

walkComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about the walks?",
)

# submitButton = html.Button("Submit", id="submit-button", n_clicks=0)
submitButton = html.A(
    html.Button("Submit", className="submit-button", id="rsubmit-button", n_clicks=0),
    href="/apps/drop_pickup",
)


# layout
layout = html.Div(
    className="checklist-header",
    children=[
        html.H3("Food checklist"),
        foodCheckList,
        foodComment,
        html.H5("Select the meal hours"),
        foodTimeCheckList,
        html.H3("Snacks checklist"),
        snackCheckList,
        snackComment,
        html.H3("Amenity checklist"),
        amenityCheckList,
        amenityComment,
        html.H3("Select the hours for the walks"),
        walkTimeCheckList,
        walkComment,
        html.Div(submitButton),
    ],
)