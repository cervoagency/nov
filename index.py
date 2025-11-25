#import dash-core, dash-html, dash io, bootstrap
import os
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from navbar import Navbar
from layouts import (Home, questionnaire)

import app
from app import app
# Import server for deployment: hide this when in local, but should not be hidden when deploying
from app import srv as server
# Import callbacks to register them
import callbacks

app_name = os.getenv("DASH_APP_PATH","/ClarityApp")

# Layout variables, navbar, header, content, and container
nav = Navbar()
CONTENT_STYLE = {
    "marginLeft": "18rem",
}
# used to have the content show on the website
content = html.Div(id="page-content", style=CONTENT_STYLE)

# callbacks for page URLs: This determines the different URLS for the website
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname in [app_name, app_name + "/"]:
        return Home
    elif pathname.endswith("/questionnaire"):
        return questionnaire
    else:
        return Home
# Main index function that will call and return all layout variables
def index():
    layout = html.Div([
        dcc.Location(id="url"),
        # Mobile menu toggle button
        html.Button("☰", id="mobile-menu-toggle", className="mobile-menu-toggle", n_clicks=0),
        # Sidebar overlay for mobile
        html.Div(id="sidebar-overlay", className="sidebar-overlay"),
        nav,
        content
    ])
    return layout

# Set layout to index function
app.layout = index()

# Call app server
if __name__ == '__main__':
    # Replit configuration: run on 0.0.0.0:5000
    app.run_server(debug=True, host='0.0.0.0', port=5000)
