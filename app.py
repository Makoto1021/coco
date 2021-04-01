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

df = pd.read_csv("sample.csv")
TOKEN = "pk.eyJ1IjoibWFrb3RvMTAyMSIsImEiOiJja213ZmZyenUwZWRxMnZwcTFzMWwzM2dmIn0.6idG-26PNC6pwiKqbYqiXQ"
px.set_mapbox_access_token(TOKEN)
image_directory = "/Users/mmiyazaki/Documents/Coco/assets/pictures"
img_list = [f for f in listdir(image_directory) if isfile(join(image_directory, f))]

today = dt.today().replace(microsecond=0, second=0, minute=0, hour=0)
today = date(today.year, today.month, today.day)

app = dash.Dash(__name__)
application = app.server
app.title='Find a pet-sitter nearby!'
app.server.static_folder = 'static'

datePicker = dcc.DatePickerSingle(
                    id='my-date-picker-single',
                    date=today)
timeRangeMarks = {str(int(i)):{'label':str(i)+':00'} for i in range(0, 25)}

timeSlider = dcc.RangeSlider(
                            min=0,
                            max=25,
                            step=None,
                            value=[12, 18],
                            marks=timeRangeMarks
                        )  

searchButton = html.Button('Search', id='search-button', n_clicks=0)



app.layout = html.Div(
    className="app-header",
    children=[
        html.Div(
            html.H1(children='Find a pet-sitter nearby!'),
            className="app-header--title"
            ),

        html.Div(
            className="app-body",
            children = [
                html.Div(
                    className="app-body--left-panel",
                    children=[
                        html.Div(
                            datePicker,
                            className="app-body--datepicker"),
                        html.Div(
                            timeSlider,
                            className="app-body--timeslider"),
                        html.Div(
                            searchButton,
                            #id='search-button',
                            className="app-body--searchbutton"
                        ),
                        html.Div(
                            dcc.Graph(id='map'),
                            className="app-body--map")]),
            
                html.Div(
                    className="app-body--right-panel",
                    children=[
                        html.Div(
                            html.Img(
                                id='image', 
                                className="app-body--desc--image"),
                            className="app-body--right-panel-img"),
                        html.Div(
                            className="app-body--right-panel-desc",
                            children=[
                            html.H3(id='name'), 
                            html.H4(id='stars'), 
                            html.H5(id='age'),
                            html.P(id='comment')
                        ])
                        ])])
        
    ]
)

@app.callback(
    Output('map', 'figure'),
    Input('search-button', 'n_clicks')
)
def show_maps(n_clicks):
    print(n_clicks)
    if n_clicks == 0:
        fig = go.Figure()
    else:
        fig = go.Figure(go.Scattermapbox(
            lat=df['lat'].values,
            lon=df['lon'].values,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=15, symbol="dog-park"
            ),
            text=df['name'],
            customdata=df[['stars', 'id']]
        ))

        fig.update_traces(
            hovertemplate="<br>".join([
                "%{text}",
                "%{customdata[0]}",
                "<extra></extra>"
            ])
        )

        fig.update_layout(
            autosize=True,
            showlegend= False,
            hovermode='closest',
            mapbox=dict(
                accesstoken=TOKEN,
                bearing=0,
                center=dict(
                    lat=48.880460,
                    lon=2.309019
                ),
                pitch=0,
                zoom=12
            ),
            margin=dict(t=0, b=0, l=0, r=0)
        )

        fig.add_trace(go.Scattermapbox(
                lat=[48.879971],
                lon=[2.313587],
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=12,
                    color='red',
                    opacity=0.5,
                    symbol="circle"
                ),
                text="You are here!",
                hoverinfo='text'
            ))
    return fig


@app.callback(
    [
        Output('image', 'src'),
        Output('name', 'children'),
        Output('age', 'children'),
        Output('comment', 'children'),
        Output('stars', 'children')
    ],
    [
        Input('map', 'clickData')
    ]
)
def show_desc(data):
    if data is None:
        image_url = ""
        name = ""
        age = ""
        comment = ""
        stars = ""
    else:
        image = image_directory + "/" + random.choice(img_list)
        test_base64 = base64.b64encode(open(image, 'rb').read()).decode('ascii')
        image_url='data:image/jpg;base64,{}'.format(test_base64)
        id = data['points'][0]['customdata'][1]
        name = df[df['id']==id].name.values[0]
        age = "Age: " + str(df[df['id']==id].age.values[0])
        comment = df[df['id']==id].comment.values[0]
        stars = df[df['id']==id].stars.values[0]
    return image_url, name, age, comment, stars

if __name__ == '__main__':
    app.run_server(
        debug=True, 
        # host = '127.0.0.1', 
        host = '0.0.0.0',
        port=8080
        )