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

layout = html.Div(
    className="sitter-header",
    children=[
        html.H3("Pet sitters detail page"),
        dcc.Location(id="sitters-page-url", refresh=False),
        html.Div(
            html.H1(children="Find a pet-sitter nearby!"),
            className="sitter-header--title",
        ),
        html.Div(
            className="sitter-body",
            id="app-body",
            children=[
                html.Div(
                    className="sitter-body--left-panel",
                    children=[
                        html.Div(html.H4("Details"), id="details"),
                        html.Div(html.H4("Reviews")),
                        html.Div(id="reviews"),
                    ],
                ),
                html.Div(
                    className="sitter-body--right-panel",
                    children=[
                        html.Div(
                            html.Img(
                                id="chosen-image", className="sitter-body--desc--image"
                            )
                        ),
                        html.Div(id="selected-sitter"),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("reviews", "children"),
    Output("chosen-image", "src"),
    Output("selected-sitter", "children"),
    [Input("sitters-page-url", "pathname"), Input("intermediate-value", "children")],
)
def show_reivews(pathname, children):
    json_data = json.loads(children)
    print(json_data)

    id = json_data["id"]
    name = json_data["name"]

    div_left = []
    for i in range(3):
        n = random.randint(0, 19)
        text = df_reviews.values[n][0] % name
        chunk = html.Div(html.H5(text))
        div_left.append(chunk)

    image = json_data["image"]
    test_base64 = base64.b64encode(open(image, "rb").read()).decode("ascii")
    image_url = "data:image/jpg;base64,{}".format(test_base64)
    age = "Age: " + str(df[df["id"] == id].age.values[0])
    comment = df[df["id"] == id].comment.values[0]
    stars = df[df["id"] == id].stars.values[0]
    id_provided = html.H4("👌ID provided👌")
    certified = html.H4("👑CERTIFIED PET-SITTER👑")
    price = html.H3("20€ / hour")
    requestButton = html.A(
        html.Button(
            "Request", className="request-button", id="request-button", n_clicks=0
        ),
        href="/apps/checklist",
    )

    div_right = [
        html.H3(name),
        id_provided,
        certified,
        html.H4(stars),
        html.H5(age),
        price,
        requestButton,
        html.P(comment),
    ]

    return div_left, image_url, div_right