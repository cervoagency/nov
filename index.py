#import dash-core, dash-html, dash io, bootstrap
import os
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from navbar import Navbar
from layouts import (Home, questionnaire, Login)

import app
from app import app
# Import server for deployment: hide this when in local, but should not be hidden when deploying
from app import srv as server
# Import callbacks to register them
import callbacks

app_name = os.getenv("DASH_APP_PATH","/ClarityApp")

# Layout variables, navbar, header, content, and container
nav = Navbar()
# Content margin is controlled by CSS media queries in custom_styles.css
# used to have the content show on the website
content = html.Div(id="page-content")

# callbacks for page URLs: This determines the different URLS for the website
@app.callback(
    [Output("page-content", "children"), Output("navbar", "style")],
    [Input("url", "pathname"), Input("user-session-store", "data")],
    prevent_initial_call=False
)
def display_page(pathname, session_data):
    # Check if user is authenticated
    is_authenticated = session_data and session_data.get("authenticated", False)
    
    # Always show login page if not authenticated
    if not is_authenticated:
        return (Login, {"display": "none"})
    
    # If authenticated, show navbar and appropriate page
    navbar_style = {"display": "flex"}
    
    if pathname in [app_name, app_name + "/"]:
        return (Home, navbar_style)
    elif pathname.endswith("/questionnaire"):
        return (questionnaire, navbar_style)
    else:
        return (Home, navbar_style)
# Main index function that will call and return all layout variables
def index():
    layout = html.Div([
        dcc.Location(id="url"),
        # User session storage
        dcc.Store(id="user-session-store", data={}, storage_type="session"),
        # Hidden element for JS output
        html.Div(id="_js_output", style={"display": "none"}),
        # Loading screen overlay
        html.Div(id="loading-screen", className="loading-screen"),
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
