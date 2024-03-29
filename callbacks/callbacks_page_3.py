from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import plotly.graph_objects as go
from load_data import df_concatenado, df_covid_combined
from layouts.layout_page_3 import df_covid_selected, df_economic_selected
import pandas as pd


def generate_3d_correlation_graph(df, vars):
    df = df[vars].dropna()
    
    if len(vars) < 3:
        print("You need at least 3 variables.")
        return go.Figure()
    
    corr_matrix = df.corr()
    
    x_data, y_data, z_data = [], [], []
    for i, var1 in enumerate(vars):
        for j, var2 in enumerate(vars):
            if i != j:
                x_data.append(var1)
                y_data.append(var2)
                z_data.append(corr_matrix.loc[var1, var2])
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x_data,
        y=y_data,
        z=z_data,
        mode='markers',
        marker=dict(
            size=8,
            color=z_data,
            colorscale='Viridis',
            opacity=0.8,
            colorbar=dict(title='Correlation'),
        ),
        text=[f'{x}, {y}: {z:.2f}' for x, y, z in zip(x_data, y_data, z_data)],
    )])
    
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), scene=dict(
                      xaxis_title='Variable X',
                      yaxis_title='Variable Y',
                      zaxis_title='Correlación'))
    return fig

def generate_hospitalizations_heatmap(df):
    df_grouped = df.groupby(['location', 'Year'])['Weekly hospitalizations per million'].mean().reset_index()
    heatmap_data = df_grouped.pivot("location", "Year", "Weekly hospitalizations per million")
    fig = px.imshow(heatmap_data, labels=dict(x="Country", y="Year", color="Weekly Hospitalizations per Million"),
                    aspect="auto", title="Hospitalizations per Million")
    fig.update_layout(xaxis={'side': 'bottom'})
    fig.update_xaxes(tickangle=-45)

    return fig

@app.callback(
    [Output('selected-country-graph', 'figure'),
     Output('economic-bubble-chart', 'figure'),
     Output('covid-evolution-graph', 'figure'),
     Output('economic-evolution-graph', 'figure'),
     Output('inflation-evolution-graph', 'figure'),
     Output('hosp-evolution-graph', 'figure'),
     Output('covid-correlation-3d', 'figure'),
     Output('economic-correlation-3d', 'figure'),
     Output('time-scatter-plot', 'figure'),
     Output('hospitalizations-heatmap-graph', 'figure')],
    [Input('country-dropdown-page3', 'value'),
     Input('covid-vars-dropdown', 'value'),
     Input('economic-vars-dropdown', 'value'),
     Input('time-slider', 'value'),
     Input('scatter-covid-var-dropdown', 'value'),
     Input('scatter-economic-var-dropdown', 'value')]
)

def update_selected_country_graph(selected_country, selected_covid_vars, selected_economic_vars, selected_year, scatter_covid_var, scatter_economic_var):
    selected_countries = ['Chile', 'Mexico', 'Canada', 'Finland', 'France', 
                        'Romania', 'Italy', 'Morocco', 'Equatorial Guinea', 
                        'Comoros', 'South Africa', 'Jordan', 'China', 'Kuwait', 
                        'United Arab Emirates']
    # df_covid_combined['Year'] = pd.to_datetime(df_covid_combined['Year'].astype(str) + '-' + df_covid_combined['Month'].astype(str)).dt.year
    annual_covid_data = df_covid_combined.groupby(['location', 'Year'])[scatter_covid_var].mean().reset_index()
    filtered_covid_df = annual_covid_data[(annual_covid_data['Year'] == selected_year) & (annual_covid_data['location'].isin(selected_countries))]
    filtered_economic_df = df_concatenado[(df_concatenado['Year'] == selected_year) & (df_concatenado['Entity'].isin(selected_countries))]
    
    fig_time = go.Figure()
    for country in selected_countries:
        country_covid_data = filtered_covid_df[filtered_covid_df['location'] == country]
        country_economic_data = filtered_economic_df[filtered_economic_df['Entity'] == country]
        
        if not country_covid_data.empty and not country_economic_data.empty:
            fig_time.add_trace(go.Scatter(
                x=country_economic_data[scatter_economic_var],
                y=country_covid_data[scatter_covid_var],
                mode='markers',
                marker=dict(size=10),
                name=country
            ))
    
    fig_time.update_layout(
    title=f'Relationship between {scatter_economic_var} and {scatter_covid_var} in {selected_year} for selected countries',
    xaxis_title=scatter_economic_var,
    yaxis_title=scatter_covid_var,
    )


    filtered_df = df_economic_selected[df_economic_selected['Entity'] == selected_country]
    fig = px.bar(filtered_df, x='Year', y=['GDP', 'Money spent in the education area','Gini Coefficient'], title=f'Data for {selected_country}')

    fig2 = px.scatter(filtered_df, 
                     x='Year', 
                     y='GDP', 
                     size='Gini Coefficient',
                     color='Money spent in the education area',
                     hover_name='Entity', 
                     title=f'Data from {selected_country}',
                     size_max=60)
    
    fig2.update_layout(transition_duration=500)

    filtered_covid_df = df_covid_combined[df_covid_combined['location'] == selected_country][selected_covid_vars]
    filtered_economic_df = df_concatenado[df_concatenado['Entity'] == selected_country][selected_economic_vars]
    
    fig5 = generate_3d_correlation_graph(filtered_covid_df, selected_covid_vars)
    fig6 = generate_3d_correlation_graph(filtered_economic_df, selected_economic_vars)
    
    fig3 = px.line(df_covid_selected, x='Date', y='Total cases per million', color='location', title='COVID-19 Total Cases Evolution for Selected Countries')
    fig4 = px.area(df_economic_selected, x='Year', y='GDP', color='Entity', line_group='Entity', title='GDP Evolution for Selected Countries')
    fig9 = px.scatter(df_covid_selected, x='Inflation rate', y='New cases per million', color='location', title='Inflation evolution according to detected cases')
    fig10 = px.area(df_covid_selected, x='Stringency index', y='Weekly hospitalizations per million', color='location', line_group='location', title='Relation between the stringency and the hospitalization rate')
    fig_heatmap = generate_hospitalizations_heatmap(df_covid_selected)




    return fig, fig2, fig3, fig4, fig9, fig10, fig5, fig6, fig_time, fig_heatmap