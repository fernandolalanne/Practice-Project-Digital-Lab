from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from load_data import df_concatenado, df_covid_combined
from layouts.layout_page_1 import variables_covid, variables_economy



selected_countries = ['Chile', 'Mexico', 'Canada', 'Finland', 'France', 'Romania', 'Italy']
df_covid_selected = df_covid_combined[df_covid_combined['location'].isin(selected_countries)]
df_economic_selected = df_concatenado[df_concatenado['Entity'].isin(selected_countries)]

def generate_covid_line_chart(df):
    fig = px.line(df, x="date", y="total_cases", color='location',
                  title="COVID-19 Total Cases Evolution")
    return fig

def generate_economic_bubble_chart(df):
    fig = px.scatter(df, x="Year", y="GDP_per_capita", size="population", color="Entity",
                     title="Economic Bubble Chart Over Time", size_max=60)
    return fig

leyenda_card = dbc.Card(
    dbc.CardBody([
        html.H4("Each country is representative of a group of countries", className="card-title"),
        html.P([
        html.Strong("Chile"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "Argentina, Brazil, Colombia, Ecuador, Guatemala, Nicaragua, Peru, Uruguay"
    ]),
    html.P([
        html.Strong("Mexico"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "Bolivia, Paraguay, Panama, Honduras"
    ]),
    html.P([
        html.Strong("Canada"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "USA"
    ]),
    html.P([
        html.Strong("France"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "Germany"
    ]),
    html.P([
        html.Strong("Italy"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "-"
    ]),
    html.P([
        html.Strong("Finland"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "Belgium"
    ]),

    html.P([
        html.Strong("Romania"), 
        html.I(className="fas fa-arrow-right", style={"margin": "0 10px"}),
        "Hungary, Poland"
    ]),
    ]),
    color="info",  # Color de la tarjeta. Puedes elegir: "primary", "secondary", "info", etc.
    inverse=True,  # Cambia el color del texto para mayor contraste con el color de fondo
    style={"maxWidth": "400px", "margin": "50px auto 0 auto"}  # Centra la tarjeta y ajusta su ancho
)



layout_page_3 = dbc.Container([
    html.H1("Representative countries Analysis"),
    dbc.Row([
        dbc.Col(html.Div("Choose a country:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='country-dropdown-page3',
            options=[{'label': country, 'value': country} for country in selected_countries],
            value=selected_countries[0]  # Valor predeterminado
        ), width=9),
    ]),
    dbc.Row(dbc.Col(dcc.Graph(id='selected-country-graph'))),
    dbc.Row(dbc.Col(html.Div("Economic Bubble Chart over Time:"))),
    dbc.Row(dbc.Col(dcc.Graph(id='economic-bubble-chart'))),
    dbc.Row([
        dbc.Col([
            html.Label('Select 3 variables to display the correlation graph:'),
            dcc.Dropdown(id='covid-vars-dropdown',
                         options=[{'label': var, 'value': var} for var in variables_covid],
                         multi=True,
                         value=['Total cases per million']  # Valores predeterminados o vacíos
                        )
        ], width=6),
        dbc.Col([
            html.Label('Select 3 variables to display the graph:'),
            dcc.Dropdown(id='economic-vars-dropdown',
                         options=[{'label': var, 'value': var} for var in variables_economy],
                         multi=True,
                         value=['GDP']  # Valores predeterminados o vacíos
                        )
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='covid-correlation-3d'), width=6),
        dbc.Col(dcc.Graph(id='economic-correlation-3d'), width=6),
    ]),
    leyenda_card,
    dbc.Row([
        dbc.Col(dcc.Graph(id='covid-evolution-graph'), width=6),
        dbc.Col(dcc.Graph(id='economic-evolution-graph'), width=6),
    ]),
], fluid=True)