import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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
            size=9, symbol="bus"
        ),
        text=df['name'],
        customdata=df[['stars', 'id', 'comment']]
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
)

app.layout = html.Div(
    children=[
        html.H1(children='Find a pet-sitter nearby!'),
        html.Div(dcc.Graph(figure=fig, id='map'), style={'width':'50%', 'display': 'inline-block'}),
        html.Div(children=[
            html.H3(id='name'), 
            html.H4(id='stars'), 
            html.H5(id='age'),
            html.P(id='comment')], style={'width':'30%','display': 'inline-block'})
        
    ]
)

@app.callback(
    [
        Output('name', 'children'),
        Output('age', 'children'),
        Output('comment', 'children'),
        Output('stars', 'children')
    ],
    [
        Input('map', 'clickData')
    ]
)
def plot_basin(data):
    if data is None:
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
    return name, age, comment, stars

if __name__ == '__main__':
    app.run_server(
        debug=True, 
        # host = '127.0.0.1', 
        host = '0.0.0.0',
        port=8080
        )