from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from load_data import df_concatenado, df_covid_combined


layout_page_2 = dbc.Container([
    html.H1("COVID-19 Data Visualization"),
    dbc.Row([
        dbc.Col(html.Div("Select a country:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='country-dropdown-page2',
            options=[{'label': country, 'value': country} for country in df_covid_combined['location'].unique()],
            value='Argentina'
        ), width=9),
    ]),
    dbc.Row([
        dbc.Col(html.Div("Select a variable:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='variable-dropdown-page2',
            options=[
                {'label': 'Total Cases', 'value': 'total_cases'},
                {'label': 'Total Deaths', 'value': 'total_deaths'},
                # Puedes agregar más variables aquí según sea necesario
            ],
            value='total_cases'  # Valor predeterminado
        ), width=9),
    ]),
    dbc.Row(dbc.Col(dcc.Graph(id='evolution-graph-page2'))),
], fluid=True)