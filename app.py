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

df = pd.read_csv("sample.csv")
TOKEN = "pk.eyJ1IjoibWFrb3RvMTAyMSIsImEiOiJja213ZmZyenUwZWRxMnZwcTFzMWwzM2dmIn0.6idG-26PNC6pwiKqbYqiXQ"
px.set_mapbox_access_token(TOKEN)

app = dash.Dash(__name__)
application = app.server
app.title='Find a pet-sitter nearby!'
app.server.static_folder = 'static'

fig = go.Figure(go.Scattermapbox(
        lat=df['lat'].values,
        lon=df['lon'].values,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9, symbol="dog-park"
        ),
        text=df['name'],
        customdata=df[['stars', 'id']]
    ))

fig.update_traces(
    hovertemplate="<br>".join([
        "%{text}",
        "%{customdata[0]}"
    ])
)

fig.update_layout(
    autosize=True,
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

app.layout = html.Div(className="app-header",
    children=[
        html.Div(html.H1(children='Find a pet-sitter nearby!'), className="app-header--title"),
        html.Div(
            dcc.Graph(figure=fig, id='map'), 
            style={'width':'50%', 'display': 'inline-block'},
            className="app-header--graph"),
        html.Div(
            className="app-header--desc",
            children=[
                html.Img(id='image', className="app-header--desc--image"),
                html.H3(id='name'), 
                html.H4(id='stars'), 
                html.H5(id='age'),
                html.P(id='comment')],
                style={'width':'30%','display': 'inline-block'})
        
    ]
)

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
        id = data['points'][0]['customdata'][1]
        name = df[df['id']==id].name.values[0]
        age = df[df['id']==id].age.values[0]
        comment = df[df['id']==id].comment.values[0]
        stars = df[df['id']==id].stars.values[0]
        image_url = "/assets/pictures/" + name + ".png"
        print(image_url)
    return image_url, name, age, comment, stars

if __name__ == '__main__':
    app.run_server(
        debug=True, 
        # host = '127.0.0.1', 
        host = '0.0.0.0',
        port=8080
        )