from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

"""
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
"""
data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)