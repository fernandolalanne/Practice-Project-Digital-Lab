from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from load_data import df_concatenado, df_covid_combined
from layouts.layout_page_1 import variables_covid, variables_economy
import plotly.graph_objects as go
import pandas as pd
import json


with open('./graph_descriptions.json') as file:
    graph_descriptions = json.load(file)

selected_countries = ['Chile', 'Mexico', 'Canada', 'Finland', 'France', 
                        'Romania', 'Italy', 'Morocco', 'Equatorial Guinea', 
                        'Comoros', 'South Africa', 'Jordan', 'China', 'Kuwait', 
                        'United Arab Emirates']
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
    color="info",
    inverse=True,
    style={"maxWidth": "400px", "margin": "50px auto 0 auto"}
)


instruction_card = dbc.Card(
    dbc.CardBody([
        html.H5("Explore the Data", className="card-title"),
        html.P("Use the drop-down menus below to select different variables and discover insights about COVID-19 and economic variables. Play with the graphs and explore!"),
    ]),
    color="success",
    outline=True,
    style={"margin-bottom": "20px"}
)

instruction_card2 = dbc.Card(
    dbc.CardBody([
        html.H5("Explore the Data", className="card-title"),
        html.P("Chooses random variables and explores their correlation!"),
    ]),
    color="success",
    outline=True,
    style={"margin-bottom": "20px"}
)


conclusiones_card = dbc.Card(
    dbc.CardBody([
        html.H2("Conclusions", className="card-title text-center", style={"marginBottom": "20px"}),
        dbc.Row([
            dbc.Col(html.P("The aim of this section is to present our main findings on the economic and health situation in the countries studied.")),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(html.Img(src="../assets/heatmap_celine.png", style={"width": "100%", "padding": "10px"})
),
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem(f"Conclusion 1: {graph_descriptions['conclusion-1']}"),
                dbc.ListGroupItem(f"Conclusion 2: {graph_descriptions['conclusion-2']}"),
                dbc.ListGroupItem(f"Conclusion 3: {graph_descriptions['conclusion-3']}"),
            ]), width=8)
        ]),
        
    ]),
    className="mb-3",
    style={"marginTop": "50px", "backgroundColor": "#f8f9fa"},  # Puedes ajustar el color de fondo
)


layout_page_3 = dbc.Container([
    html.H1("Representative countries Analysis"),
    dbc.Row([
        dbc.Col(html.Div("Choose a country:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='country-dropdown-page3',
            options=[{'label': country, 'value': country} for country in selected_countries],
            value=selected_countries[0]
        ), width=9),
    ]),
    dbc.Row(dbc.Col(dcc.Graph(id='selected-country-graph'))),
    dbc.Row(dbc.Col(html.Div("Economic performance as a function of the Giny coefficient and education expenditures:"))),
    dbc.Row(dbc.Col(dcc.Graph(id='economic-bubble-chart'))),
    html.H5("GDP evolution considering equation factors and GINI coefficient (inequality)", style={"textAlign": "center"}),
    html.P(graph_descriptions['economic-bubble-chart'], style={"textAlign": "center"}),
    instruction_card2,
    dbc.Row([
        dbc.Col([
            html.Label('Select at least 3 covid variables to display the correlation graph:'),
            dcc.Dropdown(id='covid-vars-dropdown',
                         options=[{'label': var, 'value': var} for var in variables_covid],
                         multi=True,
                         value=['Total cases per million']
                        )
        ], width=6),
        dbc.Col([
            html.Label('Select at least 3 economics variables to display the correlation graph:'),
            dcc.Dropdown(id='economic-vars-dropdown',
                         options=[{'label': var, 'value': var} for var in variables_economy],
                         multi=True,
                         value=['GDP']
                        )
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='covid-correlation-3d'), width=6),
        dbc.Col(dcc.Graph(id='economic-correlation-3d'), width=6),
    ]),
    leyenda_card,

   dbc.Row([
    dbc.Col(dcc.Graph(id='covid-evolution-graph'), width=6, style={"display": "flex", "alignItems": "center"}),
    dbc.Col(html.Div([
        html.H5("COVID-19 Evolution", style={"textAlign": "center"}),
        html.P(graph_descriptions['covid-evolution-graph'], style={"textAlign": "center"})
    ], style={
        "display": "flex", 
        "flexDirection": "column", 
        "justifyContent": "center",
        "height": "100%",
        "marginLeft": "100px",
    }), width=6),
    ], align="center"),

    dbc.Row([
    dbc.Col(html.Div([
        html.H5("Economic Evolution", style={"textAlign": "center"}),
        html.P(graph_descriptions['economic-evolution-graph'], style={"textAlign": "center"})
    ], style={
        "display": "flex", 
        "flexDirection": "column", 
        "justifyContent": "center",
        "height": "100%"
    }), width=6),
    dbc.Col(dcc.Graph(id='economic-evolution-graph'), width=6, style={"display": "flex", "alignItems": "center"}),
    ], align="center"),

    dbc.Row([
    dbc.Col(dcc.Graph(id='inflation-evolution-graph'), width=6, style={"display": "flex", "alignItems": "center"}),
    dbc.Col(html.Div([
        html.H5("Inflation Evolution", style={"textAlign": "center"}),
        html.P(graph_descriptions['inflation-evolution-graph'], style={"textAlign": "center"})
    ], style={
        "display": "flex", 
        "flexDirection": "column", 
        "justifyContent": "center",
        "height": "100%",
        "marginLeft": "100px",
    }), width=6),
], align="center"),


    dbc.Row([
    dbc.Col(html.Div([
        html.H5("Relationship between hospitalizations and restrictions", style={"textAlign": "center"}),
        html.P(graph_descriptions['hosp-evolution-graph'], style={"textAlign": "center"})
    ], style={
        "display": "flex", 
        "flexDirection": "column", 
        "justifyContent": "center",
        "height": "100%"
    }), width=6),
    dbc.Col(dcc.Graph(id='hosp-evolution-graph'), width=6, style={"display": "flex", "alignItems": "center"}),
    ], align="center"),

    instruction_card,
    dbc.Row([
        dbc.Col(html.Label("Select a COVID-19 variable for the scatter plot:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='scatter-covid-var-dropdown',
            options=[{'label': var, 'value': var} for var in variables_covid],
            value=variables_covid[0]
        ), width=9),
    ]),
    dbc.Row([
        dbc.Col(html.Label("Select an Economic variable for the scatter plot:"), width=3),
        dbc.Col(dcc.Dropdown(
            id='scatter-economic-var-dropdown',
            options=[{'label': var, 'value': var} for var in variables_economy],
            value=variables_economy[0]
        ), width=9),
    ]),
    dbc.Row([
    dbc.Col(dcc.Graph(id='time-scatter-plot'), width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Slider(
            id='time-slider',
            min=df_covid_selected['Year'].min(),
            max=df_covid_selected['Year'].max(),
            value=df_covid_selected['Year'].min(),
            marks={str(year): str(year) for year in df_covid_selected['Year'].unique()},
            step=None
        ), width=12),
    ]),
    dbc.Row([
    dbc.Col(dcc.Graph(id='hospitalizations-heatmap-graph'), width=12),
    ]),
    html.H5("Evolution of the hospitalization rates", style={"textAlign": "center"}),
    html.P(graph_descriptions['hospitalizations-heatmap-graph'], style={"textAlign": "center"}),
    conclusiones_card

], fluid=True)