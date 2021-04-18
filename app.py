import dash
import dash_core_components 
import dash_html_components as html
from dash.dependencies import Input, Output


import pandas as pd
import plotly.express as px
import api

from datetime import date

app = dash.Dash(__name__)

def clean_Data():
    con = api.connect_to_DB()
    df =pd.read_sql_query("SELECT * from Test_Data", con)
    con.close()
    return df

dff = clean_Data()

print(dff[:5])

app.layout = html.Div([
    html.H1("IOT Dashboard", style={'text-align': 'center'}),

    dash_core_components.DatePickerRange(
        id="my-date-picker-range",
        min_date_allowed=date(2021, 4, 17),
        max_date_allowed=date(2021, 12, 31),
        start_date=date.today(),
        end_date=date(2021, 8, 25)
    ),
    
    html.Br(),

    dash_core_components.Graph(id="temp-chart"),
    dash_core_components.Graph(id="humidity-chart")
])

@app.callback(
    [Output(component_id="temp-chart", component_property="figure"),
    Output(component_id="humidity-chart", component_property="figure")],
    [Input(component_id="my-date-picker-range", component_property="start_date"),
    Input(component_id="my-date-picker-range", component_property="end_date")]
)

def update_graph(start_date, end_date):
    print(start_date,end_date)

    fig_1 = px.line(dff, 
        x="timestamp", y="temperature")
    fig_2 = px.line(dff, 
        x="timestamp", y="humidity")

    return fig_1 , fig_2

if __name__ == "__main__":
    app.run_server(debug=True)