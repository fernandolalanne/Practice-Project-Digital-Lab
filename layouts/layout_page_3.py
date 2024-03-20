from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from load_data import df_concatenado, df_covid_combined
from layouts.layout_page_1 import variables_covid, variables_economy
import plotly.graph_objects as go




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
    color="info",
    inverse=True,
    style={"maxWidth": "400px", "margin": "50px auto 0 auto"}
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
        dbc.Col(dcc.Graph(id='covid-evolution-graph'), width=6),
        dbc.Col(dcc.Graph(id='economic-evolution-graph'), width=6),
        dbc.Col(dcc.Graph(id='inflation-evolution-graph'), width=6),
        dbc.Col(dcc.Graph(id='Trade-evolution-graph'), width=6),
    ]),
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


], fluid=True)