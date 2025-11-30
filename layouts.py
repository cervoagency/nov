import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import data
import plotly.graph_objects as go
from data import final_data

# Login/Signup Layout - Clean & Responsive
Login = html.Div([
    dbc.Container([
        dbc.Row([
            # Left Column - Branding (hidden on mobile)
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H1("Clarity", style={
                            "fontSize": "4rem",
                            "fontWeight": "700",
                            "background": "linear-gradient(135deg, #FFFFFF 0%, rgba(255,255,255,0.8) 100%)",
                            "WebkitBackgroundClip": "text",
                            "WebkitTextFillColor": "transparent",
                            "marginBottom": "1rem"
                        }),
                        html.P("By Nisar Solutions", style={
                            "color": "rgba(255,255,255,0.9)",
                            "fontSize": "1.2rem",
                            "fontWeight": "500",
                            "marginBottom": "2rem"
                        }),
                        html.Hr(style={
                            "borderColor": "rgba(255,255,255,0.3)",
                            "margin": "2rem 0"
                        }),
                        html.P("Powerful financial insights and analysis tools for modern businesses", style={
                            "color": "rgba(255,255,255,0.8)",
                            "fontSize": "1.1rem",
                            "lineHeight": "1.8",
                            "maxWidth": "450px"
                        }),
                        html.Ul([
                            html.Li("📊 Interactive data visualization", style={"marginBottom": "1rem"}),
                            html.Li("💼 Comprehensive financial analysis", style={"marginBottom": "1rem"}),
                            html.Li("⚡ Real-time insights", style={"marginBottom": "1rem"}),
                        ], style={
                            "color": "rgba(255,255,255,0.9)",
                            "fontSize": "1rem",
                            "marginTop": "2rem",
                            "listStyle": "none",
                            "padding": "0"
                        })
                    ], style={
                        "padding": "3rem",
                    })
                ], style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "minHeight": "100vh"
                })
            ], xs=0, sm=0, md=6, lg=6, className="d-none d-md-block"),

            # Right Column - Form
            dbc.Col([
                html.Div([
                    html.Div([
                        # Logo for mobile (shown only on small screens)
                        html.Div([
                            html.H2("Clarity", style={
                                "color": "var(--primary-color)",
                                "fontWeight": "700",
                                "marginBottom": "0.5rem",
                                "textAlign": "center"
                            }),
                            html.P("By Nisar Solutions", style={
                                "color": "var(--text-secondary)",
                                "textAlign": "center",
                                "marginBottom": "2rem",
                                "fontSize": "0.9rem"
                            }),
                        ], className="d-md-none", style={"marginBottom": "2rem"}),

                        # Form Title
                        html.H2("Welcome Back", id="auth-title", style={
                            "marginBottom": "0.5rem",
                            "color": "var(--text-primary)",
                            "fontSize": "2rem",
                            "fontWeight": "700"
                        }),
                        html.P("Login or Sign up to continue", id="auth-subtitle", style={
                            "color": "var(--text-secondary)",
                            "marginBottom": "2rem"
                        }),

                        # Error message
                        html.Div(id="auth-error", style={
                            "color": "#dc2626",
                            "fontSize": "0.875rem",
                            "marginBottom": "1rem",
                            "padding": "0.75rem",
                            "backgroundColor": "#fee2e2",
                            "borderRadius": "0.5rem",
                            "display": "none"
                        }),

                        # Email input
                        html.Div([
                            html.Label("Email", style={
                                "marginBottom": "0.5rem",
                                "fontWeight": "500",
                                "display": "block",
                                "color": "var(--text-primary)"
                            }),
                            dcc.Input(
                                id="auth-email",
                                type="email",
                                placeholder="name@example.com",
                                autoComplete="email",
                                style={
                                    "width": "100%",
                                    "padding": "0.75rem 1rem",
                                    "borderRadius": "0.5rem",
                                    "border": "2px solid #e5e7eb",
                                    "fontSize": "1rem",
                                    "transition": "all 0.3s ease",
                                    "fontFamily": "Inter, sans-serif",
                                    "boxSizing": "border-box"
                                }
                            ),
                        ], style={"marginBottom": "1.5rem"}),

                        # Password input
                        html.Div([
                            html.Label("Password", style={
                                "marginBottom": "0.5rem",
                                "fontWeight": "500",
                                "display": "block",
                                "color": "var(--text-primary)"
                            }),
                            dcc.Input(
                                id="auth-password",
                                type="password",
                                placeholder="Enter your password",
                                autoComplete="current-password",
                                style={
                                    "width": "100%",
                                    "padding": "0.75rem 1rem",
                                    "borderRadius": "0.5rem",
                                    "border": "2px solid #e5e7eb",
                                    "fontSize": "1rem",
                                    "transition": "all 0.3s ease",
                                    "fontFamily": "Inter, sans-serif",
                                    "boxSizing": "border-box"
                                }
                            ),
                        ], style={"marginBottom": "1.5rem"}),

                        # Confirm Password (hidden by default)
                        html.Div([
                            html.Label("Confirm Password", style={
                                "marginBottom": "0.5rem",
                                "fontWeight": "500",
                                "display": "block",
                                "color": "var(--text-primary)"
                            }),
                            dcc.Input(
                                id="auth-confirm-password",
                                type="password",
                                placeholder="Confirm your password",
                                autoComplete="new-password",
                                style={
                                    "width": "100%",
                                    "padding": "0.75rem 1rem",
                                    "borderRadius": "0.5rem",
                                    "border": "2px solid #e5e7eb",
                                    "fontSize": "1rem",
                                    "transition": "all 0.3s ease",
                                    "fontFamily": "Inter, sans-serif",
                                    "boxSizing": "border-box"
                                }
                            ),
                        ], id="confirm-password-section", style={"marginBottom": "1.5rem", "display": "none"}),

                        # Submit button
                        html.Button(
                            "Sign In",
                            id="auth-submit-btn",
                            n_clicks=0,
                            style={
                                "width": "100%",
                                "padding": "0.875rem 1rem",
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

                        # Forgot password link
                        html.Div([
                            html.Span("Forgot password? ", style={
                                "color": "var(--text-secondary)",
                                "fontSize": "0.9rem"
                            }),
                            html.A(
                                "Reset it",
                                id="reset-password-link",
                                n_clicks=0,
                                style={
                                    "color": "var(--primary-color)",
                                    "textDecoration": "underline",
                                    "fontSize": "0.9rem",
                                    "fontWeight": "500",
                                    "cursor": "pointer",
                                    "background": "none",
                                    "border": "none",
                                    "padding": "0"
                                }
                            )
                        ], style={
                            "textAlign": "center",
                            "marginTop": "1rem",
                            "marginBottom": "1.5rem"
                        }),

                        # Divider
                        html.Div([
                            html.Hr(style={
                                "borderColor": "#e5e7eb",
                                "margin": "1.5rem 0"
                            }),
                        ]),

                        # Sign up/Sign in toggle
                        html.Div([
                            html.Span(id="toggle-text", children="Don't have an account? ", style={
                                "color": "var(--text-secondary)",
                                "fontSize": "0.95rem"
                            }),
                            html.A(
                                "Sign Up",
                                id="toggle-signup-btn",
                                n_clicks=0,
                                style={
                                    "color": "var(--primary-color)",
                                    "textDecoration": "underline",
                                    "fontSize": "0.95rem",
                                    "fontWeight": "600",
                                    "cursor": "pointer",
                                    "background": "none",
                                    "border": "none",
                                    "padding": "0"
                                }
                            )
                        ], style={"textAlign": "center"}),
                    ], style={
                        "backgroundColor": "white",
                        "padding": "2.5rem",
                        "borderRadius": "1rem",
                        "boxShadow": "0 10px 25px rgba(0, 0, 0, 0.1)",
                        "maxWidth": "450px",
                        "width": "100%"
                    }),
                ], style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "minHeight": "100vh",
                    "padding": "2rem 1rem"
                })
            ], xs=12, sm=12, md=6, lg=6)
        ], style={"minHeight": "100vh", "margin": "0"}),
    ], fluid=True, style={"padding": "0"}),

    # Reset Password Modal (Simple & Clean)
    dbc.Modal([
        dbc.ModalHeader(
            dbc.ModalTitle("Reset Password", style={"color": "var(--text-primary)"}),
            close_button=True
        ),
        dbc.ModalBody([
            html.P(
                "Enter your email address and we'll send you instructions to reset your password.",
                style={
                    "color": "var(--text-secondary)",
                    "marginBottom": "1.5rem",
                    "lineHeight": "1.6"
                }
            ),
            html.Div([
                html.Label("Email Address", style={
                    "marginBottom": "0.5rem",
                    "fontWeight": "500",
                    "display": "block"
                }),
                dcc.Input(
                    id="reset-email",
                    type="email",
                    placeholder="name@example.com",
                    style={
                        "width": "100%",
                        "padding": "0.75rem 1rem",
                        "borderRadius": "0.5rem",
                        "border": "2px solid #e5e7eb",
                        "fontSize": "1rem",
                        "boxSizing": "border-box"
                    }
                ),
            ]),
            html.Div(id="reset-message", style={
                "marginTop": "1rem",
                "fontSize": "0.875rem",
                "display": "none"
            }),
        ]),
        dbc.ModalFooter([
            dbc.Button(
                "Cancel",
                id="cancel-reset-btn",
                color="secondary",
                outline=True,
                n_clicks=0
            ),
            dbc.Button(
                "Send Reset Link",
                id="submit-reset-btn",
                color="primary",
                n_clicks=0
            ),
        ]),
    ], id="reset-modal", is_open=False, centered=True),
], style={
    "background": "linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%)",
    "minHeight": "100vh",
    "padding": "0",
    "margin": "0"
})

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
