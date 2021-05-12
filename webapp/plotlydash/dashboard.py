import dash
import dash_core_components 
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import api

from datetime import date

def init_dashboard(server):
    #creating a dash Dashboard

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/css/dashboard.css"
        ]
    )    
    
    dff = clean_Data()

    #creating the dash layout 
    dash_app.layout = html.Div([
        html.H1("IOT Dashboard"),
        
        dash_core_components.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(2021, 4, 17),
            max_date_allowed=date(2021, 12, 31),
            start_date=date.today(),
            end_date=date(2021, 8, 25)
        ),
        
        html.Br(),

        dash_core_components.Graph(
            id="temp-chart"
            ),
        dash_core_components.Graph(
            id="humidity-chart"
            ),

        init_callbacks(dash_app, dff),
        
    ])
    
    return dash_app.server

def init_callbacks(dash_app, dff):
    @dash_app.callback(
        [Output(component_id="temp-chart", component_property="figure"),
        Output(component_id="humidity-chart", component_property="figure")],
        [Input(component_id="my-date-picker-range", component_property="start_date"),
        Input(component_id="my-date-picker-range", component_property="end_date")]
    )

    def update_graph(start_date, end_date):
        
        dff_filtered = dff.loc[start_date : end_date]
        
        fig_1 = px.line(dff_filtered, 
            x="timestamp", y="temperature", title="Temp chart")
        fig_2 = px.line(dff_filtered, 
            x="timestamp", y=["co", "lpg","smoke"],title="Gases chart" ,log_y=True)

        return fig_1 , fig_2



def clean_Data():
    con = api.connect_to_DB()
    df = pd.read_sql_query("SELECT * from data", con)
    con.close()
    
    df["id"] = pd.to_datetime(df["timestamp"])
    df = df.set_index(["id"])
    df.sort_index(inplace=True, ascending=True)
    return df

if __name__ == "__main__":
    dff = clean_Data()
    dash_app.run_server(debug=True)