import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import data
import plotly.graph_objects as go
from data import final_data

Home = html.Div(
    [html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1("Home- demo", style={"text-align": "center"})],
    className="mx-2")

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
    html.H2("Calcul"),
    #
    dcc.Dropdown(options=('choice_entreprise[0]', 'choice_entreprise[1]'), value="choice_entreprise[0]",
                 id='choix_type_compagnie'),
    #
    dbc.Row([dbc.Col(dbc.FormText("Montant 1:"), width="auto"), ], ),
    dbc.Row([dbc.Col(dcc.Input(id='profit_an_dernier', type="number", style={'padding': 10, 'height': 35, 'width': '100%'}), ),], ),
    #
    dbc.Row([dbc.Col(dbc.FormText("Montant 2:"), width="auto"), ], ),
    dbc.Row([dbc.Col(dcc.Input(id='profit_prev_ann_courante', type="number", style={'padding': 10, 'height': 35, 'width': '100%'}), ),], ),
    #
    dbc.Row([dbc.Col(dbc.FormText("Montant 3:"), width="auto"), ], ),
    dbc.Row([dbc.Col(dcc.Input(id='revenus_an_dernier', type="number", style={'padding': 10, 'height': 35, 'width': '100%'}), ),], ),
    #
    dbc.Row([dbc.Col(dbc.FormText("Nombre 1:"), width="auto"), ], ),
    dbc.Row([dbc.Col(dcc.Input(id='nombreemployes', type="number", style={'padding': 10, 'height': 35, 'width': '100%'}),)],),
    #
    dbc.Row([dbc.Col(dbc.FormText("Montant 4"), width="auto"), ]),
    dbc.Row([dbc.Col(dcc.Input(id='montantloyer', type="number", style={'padding': 10, 'height': 35, 'width': '100%'}),),],),
    #
    dbc.Row([dbc.Col(dbc.FormText("Secteur"), width="auto"),],),
    dbc.Row([dbc.Col(dcc.Dropdown(options=["Montreal", "Toronto"], value="Montreal",id="secteur_activité"),),]),
    html.Button("Envoyer", id="submit-btn", n_clicks=0, style={"marginRight": "15px"}),
    html.Hr(),
   # html.H4("Preview"),
    dbc.Row([
        dbc.Col(html.Div(dcc.Graph(id='piechart', figure=piechart, config={'displaylogo': False, 'editable': True})),width=4),
        dbc.Col(html.Div(dcc.Graph(id='indic1', figure=indic1, config={'displaylogo': False, 'editable': True})),width=4),
        dbc.Col(html.Div(dcc.Graph(id='indic2', figure=indic2,config={'displaylogo': False, 'editable': True})),width=4),
    ])
])
