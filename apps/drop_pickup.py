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