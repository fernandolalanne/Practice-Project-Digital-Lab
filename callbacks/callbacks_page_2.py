from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
from load_data import df_concatenado, df_covid_combined


@app.callback(
    Output('evolution-graph-page2', 'figure'),
    [Input('country-dropdown-page2', 'value'),
     Input('variable-dropdown-page2', 'value'),
    ]
)
def update_graph_page2(selected_country, selected_variable):
    filtered_df = df_covid_combined[df_covid_combined['location'] == selected_country]
    
    
    fig = px.bar(filtered_df, x='Month', y=selected_variable, color='Year',
                    title=f"Evolution od {selected_variable} in {selected_country} per Year and Month")
    
    return fig