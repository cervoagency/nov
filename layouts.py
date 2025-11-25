import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import data
import plotly.graph_objects as go
from data import final_data

# Login/Signup Layout
Login = html.Div([
    html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        # Left side - Branding and info
                        html.Div([
                            html.H1("Clarity", style={
                                "color": "white",
                                "fontSize": "3.5rem",
                                "fontWeight": "700",
                                "marginBottom": "1rem"
                            }),
                            html.P("By Nisar Solutions", style={
                                "color": "rgba(255,255,255,0.8)",
                                "fontSize": "1.1rem",
                                "marginBottom": "2rem"
                            }),
                            html.P("Powerful financial insights and analysis tools for modern businesses", style={
                                "color": "rgba(255,255,255,0.7)",
                                "fontSize": "1rem",
                                "lineHeight": "1.6",
                                "maxWidth": "400px"
                            })
                        ], style={"marginTop": "4rem"})
                    ], className="login-left-section"),
                ], xs=12, sm=12, md=6, lg=6, style={"display": "flex", "alignItems": "center"}),
                
                dbc.Col([
                    html.Div([
                        # Right side - Form
                        html.Form([
                            html.H2("Welcome Back", id="auth-title", style={
                                "marginBottom": "0.5rem",
                                "color": "var(--text-primary)",
                                "fontSize": "2rem",
                                "fontWeight": "700"
                            }),
                            html.P("Sign in to your account to continue", id="auth-subtitle", style={
                                "color": "var(--text-secondary)",
                                "marginBottom": "2rem"
                            }),
                            
                            # Email/Username input
                            html.Div([
                                html.Label("Email or Username", style={"marginBottom": "0.5rem", "fontWeight": "500"}),
                                dcc.Input(
                                    id="auth-email",
                                    type="text",
                                    placeholder="Enter your email or username",
                                    className="auth-input",
                                    autoComplete="username",
                                    style={
                                        "width": "100%",
                                        "padding": "0.75rem 1rem",
                                        "borderRadius": "0.5rem",
                                        "border": "1px solid #e5e7eb",
                                        "fontSize": "1rem",
                                        "marginBottom": "1.5rem",
                                        "fontFamily": "Inter, sans-serif",
                                        "boxSizing": "border-box"
                                    }
                                ),
                            ]),
                            
                            # Password input
                            html.Div([
                                html.Label("Password", style={"marginBottom": "0.5rem", "fontWeight": "500"}),
                                dcc.Input(
                                    id="auth-password",
                                    type="password",
                                    placeholder="Enter your password",
                                    className="auth-input",
                                    autoComplete="current-password",
                                    style={
                                        "width": "100%",
                                        "padding": "0.75rem 1rem",
                                        "borderRadius": "0.5rem",
                                        "border": "1px solid #e5e7eb",
                                        "fontSize": "1rem",
                                        "marginBottom": "1.5rem",
                                        "fontFamily": "Inter, sans-serif",
                                        "boxSizing": "border-box"
                                    }
                                ),
                            ], id="password-section"),
                            
                            # Confirm Password (hidden for login, shown for signup)
                            html.Div([
                                html.Label("Confirm Password", style={"marginBottom": "0.5rem", "fontWeight": "500"}),
                                dcc.Input(
                                    id="auth-confirm-password",
                                    type="password",
                                    placeholder="Confirm your password",
                                    className="auth-input",
                                    autoComplete="new-password",
                                    style={
                                        "width": "100%",
                                        "padding": "0.75rem 1rem",
                                        "borderRadius": "0.5rem",
                                        "border": "1px solid #e5e7eb",
                                        "fontSize": "1rem",
                                        "marginBottom": "1.5rem",
                                        "fontFamily": "Inter, sans-serif",
                                        "boxSizing": "border-box"
                                    }
                                ),
                            ], id="confirm-password-section", style={"display": "none"}),
                            
                            # Error message
                            html.Div(id="auth-error", style={
                                "color": "#dc2626",
                                "fontSize": "0.875rem",
                                "marginBottom": "1rem",
                                "display": "none"
                            }),
                            
                            # Submit button
                            html.Button(
                                "Sign In",
                                id="auth-submit-btn",
                                n_clicks=0,
                                type="button",
                                style={
                                    "width": "100%",
                                    "padding": "0.75rem 1rem",
                                    "backgroundColor": "var(--primary-color)",
                                    "color": "white",
                                    "border": "none",
                                    "borderRadius": "0.5rem",
                                    "fontSize": "1rem",
                                    "fontWeight": "600",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                    "marginBottom": "1rem"
                                },
                                className="auth-btn"
                            ),
                            
                            # Toggle between sign in and sign up
                            html.Div([
                                html.Span("Don't have an account? ", style={"color": "var(--text-secondary)"}),
                                html.Button(
                                    "Sign Up",
                                    id="toggle-signup-btn",
                                    n_clicks=0,
                                    type="button",
                                    style={
                                        "background": "none",
                                        "border": "none",
                                        "color": "var(--primary-color)",
                                        "cursor": "pointer",
                                        "fontSize": "1rem",
                                        "fontWeight": "600",
                                        "textDecoration": "underline"
                                    }
                                )
                            ], style={"textAlign": "center", "marginTop": "1rem"}),
                        ], style={
                            "backgroundColor": "white",
                            "padding": "2rem",
                            "borderRadius": "1rem",
                            "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.07)",
                            "maxWidth": "400px",
                            "margin": "0 auto"
                        }),
                    ], style={"display": "flex", "alignItems": "center", "minHeight": "100vh"})
                ], xs=12, sm=12, md=6, lg=6)
            ], style={"minHeight": "100vh"}),
        ], fluid=True, style={"padding": "0"})
    ], style={
        "background": "linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%)",
        "minHeight": "100vh"
    }),
], style={"padding": "0", "margin": "0"})

Home = html.Div([
    html.Div([
        html.H1("Welcome to Clarity", className="hero-title"),
        html.P(
            "Powerful financial insights and analysis tools for modern businesses",
            className="hero-subtitle"
        ),
    ], className="hero-section fade-in"),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div("📊", style={"fontSize": "3rem", "marginBottom": "1rem"}),
                html.H3("Data Visualization", style={"marginBottom": "1rem"}),
                html.P(
                    "Interactive charts and graphs that bring your financial data to life",
                    style={"color": "var(--text-secondary)"}
                ),
            ], className="modern-card fade-in")
        ], xs=12, sm=12, md=4, lg=4),
        dbc.Col([
            html.Div([
                html.Div("💼", style={"fontSize": "3rem", "marginBottom": "1rem"}),
                html.H3("Business Insights", style={"marginBottom": "1rem"}),
                html.P(
                    "Make informed decisions with comprehensive financial analysis",
                    style={"color": "var(--text-secondary)"}
                ),
            ], className="modern-card fade-in")
        ], xs=12, sm=12, md=4, lg=4),
        dbc.Col([
            html.Div([
                html.Div("⚡", style={"fontSize": "3rem", "marginBottom": "1rem"}),
                html.H3("Real-time Updates", style={"marginBottom": "1rem"}),
                html.P(
                    "Get instant feedback and calculations as you input your data",
                    style={"color": "var(--text-secondary)"}
                ),
            ], className="modern-card fade-in")
        ], xs=12, sm=12, md=4, lg=4),
    ], style={"marginTop": "2rem"}),
], style={"padding": "0"})

# Chart Définitions
piechart=go.Figure()
# indicator
indic1=go.Figure()
indic2=go.Figure()

montant_impot_idx_ISIBA_calc = 90
montant_impot_idx_ISIBA_current = 100

##### piechart
piechart = go.Figure(go.Pie(labels=final_data["Emplacement"], values=final_data["montant"], hole=0.5))

##### indicators

indic1=go.Figure()

indic1.add_trace(go.Indicator(mode="number+delta+gauge",number={'font': {'size': 50}, 'valueformat': '.0f'},
            value=montant_impot_idx_ISIBA_current,delta={'reference': montant_impot_idx_ISIBA_calc},
            gauge={ 'shape': "bullet",
                'axis': {'range': [None, montant_impot_idx_ISIBA_calc], },
                'bar': {'color': "#505bf0"},
                'threshold': {
                    'line': {'color': "#001a72", 'width': 5},
                    'thickness': 0.75,
                    'value': montant_impot_idx_ISIBA_calc}},))
indic2 = go.Figure()
indic2.add_trace(go.Indicator(mode="number",number={'font': {'size': 50}, 'valueformat': '.0f'},value=montant_impot_idx_ISIBA_calc,
            ))

######


questionnaire=html.Div([
    html.H2("Financial Dashboard", className="section-header"),
    
    html.Div([
        html.H4("Company Information", style={"marginBottom": "1.5rem", "color": "var(--text-primary)"}),
        
        dbc.Row([
            dbc.Col([
                dbc.FormText("Company Type", className="form-label"),
                dcc.Dropdown(
                    options=[
                        {'label': 'Enterprise Type 1', 'value': 'choice_entreprise[0]'},
                        {'label': 'Enterprise Type 2', 'value': 'choice_entreprise[1]'}
                    ],
                    value="choice_entreprise[0]",
                    id='choix_type_compagnie'
                ),
            ], md=12),
        ], style={"marginBottom": "1.5rem"}),
        
        dbc.Row([
            dbc.Col([
                dbc.FormText("Last Year Profit", className="form-label"),
                dcc.Input(id='profit_an_dernier', type="number", placeholder="Enter amount...", style={'width': '100%'}),
            ], xs=12, sm=12, md=6, lg=6),
            dbc.Col([
                dbc.FormText("Current Year Projected Profit", className="form-label"),
                dcc.Input(id='profit_prev_ann_courante', type="number", placeholder="Enter amount...", style={'width': '100%'}),
            ], xs=12, sm=12, md=6, lg=6),
        ], style={"marginBottom": "1.5rem"}),
        
        dbc.Row([
            dbc.Col([
                dbc.FormText("Last Year Revenue", className="form-label"),
                dcc.Input(id='revenus_an_dernier', type="number", placeholder="Enter amount...", style={'width': '100%'}),
            ], xs=12, sm=12, md=6, lg=6),
            dbc.Col([
                dbc.FormText("Number of Employees", className="form-label"),
                dcc.Input(id='nombreemployes', type="number", placeholder="Enter number...", style={'width': '100%'}),
            ], xs=12, sm=12, md=6, lg=6),
        ], style={"marginBottom": "1.5rem"}),
        
        dbc.Row([
            dbc.Col([
                dbc.FormText("Monthly Rent", className="form-label"),
                dcc.Input(id='montantloyer', type="number", placeholder="Enter amount...", style={'width': '100%'}),
            ], xs=12, sm=12, md=6, lg=6),
            dbc.Col([
                dbc.FormText("Business Sector", className="form-label"),
                dcc.Dropdown(
                    options=[
                        {'label': 'Montreal', 'value': 'Montreal'},
                        {'label': 'Toronto', 'value': 'Toronto'}
                    ],
                    value="Montreal",
                    id="secteur_activité"
                ),
            ], xs=12, sm=12, md=6, lg=6),
        ], style={"marginBottom": "2rem"}),
        
        html.Button("Calculate Results", id="submit-btn", n_clicks=0),
    ], className="form-section fade-in"),
    
    html.H4("Analytics Overview", className="section-header", style={"marginTop": "3rem"}),
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.Graph(id='piechart', figure=piechart, config={'displaylogo': False, 'editable': True, 'responsive': True}),
                className="chart-container"
            ),
            xs=12, sm=12, md=4, lg=4
        ),
        dbc.Col(
            html.Div(
                dcc.Graph(id='indic1', figure=indic1, config={'displaylogo': False, 'editable': True, 'responsive': True}),
                className="chart-container"
            ),
            xs=12, sm=12, md=4, lg=4
        ),
        dbc.Col(
            html.Div(
                dcc.Graph(id='indic2', figure=indic2, config={'displaylogo': False, 'editable': True, 'responsive': True}),
                className="chart-container"
            ),
            xs=12, sm=12, md=4, lg=4
        ),
    ], className="fade-in")
], style={"padding": "0"})
