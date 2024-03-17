from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
from load_data import df_concatenado, df_covid_combined


@app.callback(
    [Output('country-selected', 'children'),
     Output('feature-graph', 'figure'),
     Output('monthly-data-graph', 'figure'),  # Añadido para actualizar el gráfico mensual
     Output('analysis-box', 'children')],
    [Input('world-map', 'clickData'),
     Input('variable-dropdown', 'value'),
     Input('monthly-data-dropdown', 'value')])  # Añadido para escuchar cambios en el dropdown mensual
def update_graph(clickData, selected_variable, selected_monthly_variable):
    if clickData is None:
        analysis_text = 'Choose a country and a variable to see the analysis.'
        return 'Choose a country', {}, {}, analysis_text
    else:
        country_name = clickData['points'][0]['location']
        df_filtered = df_concatenado[df_concatenado['Entity'] == country_name]
        df_filtered_monthly = df_covid_combined[df_covid_combined['location'] == country_name]

        fig = px.line(df_filtered, x='Year', y=selected_variable, title=f'Annual {selected_variable} for {country_name}',
                      template="plotly_white")
        fig.update_layout(
            title={'text': f'Annual {selected_variable} for {country_name}', 'x': 0.5, 'xanchor': 'center'},
            xaxis_title="Year",
            yaxis_title=selected_variable,
            height=400,  # Ajusta el tamaño del gráfico
            font=dict(size=12)  # Ajusta el tamaño del texto global, incluyendo los títulos de los ejes
        )

        fig_monthly = px.line(df_filtered_monthly, x='Date', y=selected_monthly_variable,
                      title=f'Monthly {selected_monthly_variable} in {country_name}', template="plotly_white",
                      color_discrete_sequence=['violet'])  # Est

        fig_monthly.update_layout(
            title={'text': f'Monthly {selected_monthly_variable} in {country_name}', 'x': 0.5, 'xanchor': 'center'},
            xaxis_title="Date",
            yaxis_title=selected_monthly_variable,
            height=400,  # Ajusta el tamaño del gráfico para que coincida con el otro gráfico
            font=dict(size=12)  # Ajusta el tamaño del texto global, incluyendo los títulos de los ejes
        )
        # fig_monthly.update_xaxes(dtick="M1", tickformat="%Y/%m", ticklabelmode="period")


        analysis_text = f"Analysis for {country_name}: Here you can provide insights into the {selected_variable} trends over time..."
        
        return f'Country: {country_name}', fig, fig_monthly, analysis_text