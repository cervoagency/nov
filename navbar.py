# Import Bootstrap from Dash
import os
import dash_bootstrap_components as dbc
from dash import html
from app import app

app_name = os.getenv("DASH_APP_PATH", "/ClarityApp")

# logo
Logo = "assets/nisar_solutions_logo_nov25.png"
# make a reuseable navitem

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "white",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


# Navigation Bar function
def Navbar():
    navbar = html.Div(
            [html.H2("Demo", className="display-4"),
             html.H4("Test"),
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=Logo, height="150px")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    #href="https://nisarsolutions.com",
                    style={"textDecoration": "none"},
                ),
             html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("Home", active="exact", href="/"),
                        dbc.NavLink("Démo", href="/questionnaire", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
                ],
        style=SIDEBAR_STYLE,
    )
    return navbar
