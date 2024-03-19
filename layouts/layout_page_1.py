from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from load_data import df_concatenado, df_covid_combined
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# Asumiendo que 'df_concatenado' y 'df_covid_combined' son cargados aquí o importados

fig_map = px.scatter_geo(df_concatenado, locations="Entity", locationmode='country names',
                         hover_name="Entity", projection="natural earth")
                         
variables_economy = ['Percentage of GDP of trade', 'Poorest decile threshold',
            'Gini Coefficient', 'Median income', 'Richest decile threshold','Money spent in the education area']
variables_covid = ['Total Deaths', 'Total cases per million',
'New cases per million', 'Stringency index', 
'Weekly hospitalizations per million','Inflation rate']

layout_page_1 = dbc.Container([
    html.H1("Economic and Social Evolution by Country"),
    dbc.Row(dbc.Col(html.Div("Select a country by clicking on the map below:"))),
    dbc.Row(dbc.Col(dcc.Graph(id='world-map', figure=fig_map))),
    html.Div(id='country-selected'),
    dbc.Row(dbc.Col(html.H4("Choose a variable to display:"))),
    dbc.Row(dbc.Col(dcc.Dropdown(
        id='variable-dropdown',
        options=[{'label': i, 'value': i} for i in variables_economy],
        value=variables_economy[0]  # default value
    ))),
    dbc.Row(dbc.Col(html.Div("Graphical representation:"))),
    dbc.Row([
        dbc.Col(dcc.Graph(id='feature-graph'), width=6),
        dbc.Col([
            html.H4("Monthly Data Visualization"),
            dcc.Dropdown(
                id='monthly-data-dropdown',
                options=[{'label': i, 'value': i} for i in variables_covid],  # Asume que la columna 3 tiene datos mensuales
                value=variables_covid[0]  # default value
            ),
            dcc.Graph(id='monthly-data-graph')  # Gráfico para datos mensuales
        ], width=6)
    ]),
    dbc.Row(dbc.Col(html.Div(id='analysis-box')))
], fluid=True)
