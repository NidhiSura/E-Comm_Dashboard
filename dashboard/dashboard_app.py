from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import requests
import pandas as pd

# Fetch data from the API
response = requests.get('http://127.0.0.1:5000/api/sales')
data = response.json()
df = pd.DataFrame(data)

# Initialize the app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': category, 'value': category} for category in df['category'].unique()],
        placeholder="Select a category",
    ),
    dcc.Graph(id='sales-chart')
])

# Callback to update the chart
@app.callback(
    Output("sales-chart", "figure"),
    [Input("dropdown", "value")]
)
def update_chart(selected_category):
    if selected_category:
        filtered_df = df[df['category'] == selected_category]
    else:
        filtered_df = df

    return {
        'data': [{
            'x': filtered_df['date'],
            'y': filtered_df['sales'],
            'type': 'bar'
        }],
        'layout': {
            'title': 'Sales Chart'
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Ecommerce Analytics Dashboard"), className="text-center")),
    dbc.Row(dbc.Col(dcc.Dropdown(...))),
    dbc.Row(dbc.Col(dcc.Graph(...)))
])