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
# Note: width is controlled by CSS media queries in custom_styles.css
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "padding": "2rem 1.5rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


# Navigation Bar function
def Navbar(id="navbar"):
    navbar = html.Div(
            [
                html.H2("Clarity", className="display-4"),
                html.H4("by Nisar Solutions"),
                html.Div(
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=Logo, height="140px")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        style={"textDecoration": "none"},
                    ),
                    className="logo-container"
                ),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("🏠 Home", active="exact", href="/"),
                        dbc.NavLink("📊 Dashboard", href="/questionnaire", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
        style=SIDEBAR_STYLE,
        className="sidebar",
        id=id
    )
    return navbar
