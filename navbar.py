# Import Bootstrap from Dash
import os
import dash_bootstrap_components as dbc
from dash import html
from app import app

app_name = os.getenv("DASH_APP_PATH", "/ClarityApp")

# logo
Logo = "assets/nisar_solutions_logo_nov25.png"

# the style arguments for the sidebar. We use position:fixed and a fixed width
# Note: width and positioning are controlled by CSS media queries in bootstrap-grid.css
SIDEBAR_STYLE = {
    "padding": "2rem 1.5rem",
    "display": "flex",
    "flexDirection": "column",
    "height": "100%",
}

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

            # Spacer to push logout button to bottom
            html.Div(style={"flex": "1"}),

            # Logout Section
            html.Hr(style={
                "borderColor": "rgba(255, 255, 255, 0.2)",
                "margin": "2rem 0 1rem 0"
            }),

            html.Button([
                html.Span("🚪 ", style={"marginRight": "0.5rem"}),
                "Logout"
            ], 
            id="logout-btn",
            n_clicks=0,
            style={
                "width": "100%",
                "padding": "0.75rem 1rem",
                "backgroundColor": "rgba(220, 38, 38, 0.1)",
                "color": "white",
                "border": "2px solid rgba(220, 38, 38, 0.3)",
                "borderRadius": "8px",
                "fontSize": "1rem",
                "fontWeight": "600",
                "cursor": "pointer",
                "transition": "all 0.3s ease",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "fontFamily": "Inter, sans-serif"
            },
            className="logout-btn"
            ),
        ],
        style=SIDEBAR_STYLE,
        className="sidebar",
        id=id
    )
    return navbar