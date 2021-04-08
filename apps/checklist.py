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
        {"label": "I bring my own food!", "value": "bringFood"},
    ],
    labelStyle=dict(display="block"),
    id="food",
)

foodComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his food?", id="food-comment"
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
    id="food-time-checklist",
)

snackCheckList = dcc.Checklist(
    options=[
        {"label": "I bring my own snacks!", "value": "bringSnacks"},
    ],
    labelStyle=dict(display="block"),
    id="snack-checklist",
)

snackComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his snacks?", id="snack-comment"
)

amenityCheckList = dcc.Checklist(
    options=[
        {"label": "I bring my own toys!", "value": "bringToys"},
        {"label": "I bring my own leash!", "value": "bringLeash"},
        {"label": "I bring my own toilette sheets!", "value": "bringSheets"},
        {"label": "I bring my own blankets/bed!", "value": "bringBed"},
    ],
    labelStyle=dict(display="block"),
    id="amenity-checklist",
)

amenityComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about his ammenities?",
    id="amenity-comment",
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
    id="walktime-checklist",
)

walkComment = dcc.Textarea(
    placeholder="Do you want to leave a comment about the walks?", id="walk-comment"
)

# submitButton = html.Button("Submit", id="submit-button", n_clicks=0)
nextButton = html.A(
    html.Button("Next", className="next-button", id="next-button", n_clicks=0),
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
        html.Div(nextButton),
    ],
)

"""
@app.callback(
    [Output("intermediate-value-2", "children")],
    [Input("intermediate-value-2", "children"), Input("food", "value")],
)
def update_foodChecklist(data, value):
    print("food-checklist", value)
    json_data = json.loads(data)
    json_data["foodCheck"] = value
    updated_json = json.dumps(json_data)
    print("updated_json", updated_json)
    return updated_json



@app.callback(
    [Output("intermediate-value-2", "children")],
    [
        Input("food-checklist", "value"),
        Input("food-comment", "value"),
        Input("food-time-checklist", "value"),
        Input("snack-checklist", "value"),
        Input("snack-comment", "value"),
        Input("amenity-checklist", "value"),
        Input("amenity-comment", "value"),
        Input("walktime-checklist", "value"),
        Input("walk-comment", "value"),
        Input("next-button", "n_clicks"),
    ],
)
def submit_checklist1(
    foodCheck,
    foodComment,
    foodTime,
    snackCheck,
    snackComment,
    amenityCheck,
    amenityComment,
    walkTimeCheck,
    walkComment,
    n_clicks,
):
    intermediate_value = {
        "foodCheck": foodCheck,
        "foodComment": foodComment,
        "foodTime": foodTime,
        "snackCheck": snackCheck,
        "snackComment": snackComment,
        "amenityCheck": amenityCheck,
        "amenityComment": amenityComment,
        "walkTimeCheck": walkTimeCheck,
        "walkComment": walkComment,
    }
    print("intermediate_value is", intermediate_value)
    intermediate_value = json.dumps(intermediate_value)
    return intermediate_value
"""