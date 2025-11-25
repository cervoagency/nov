import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import data
import plotly.graph_objects as go
from data import final_data

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
