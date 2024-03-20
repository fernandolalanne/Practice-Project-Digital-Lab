from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
from load_data import df_concatenado, df_covid_combined
import plotly.graph_objects as go


@app.callback(
    [Output('country-selected', 'children'),
     Output('feature-graph', 'figure'),
     Output('monthly-data-graph', 'figure')],
    [Input('world-map', 'clickData'),
     Input('variable-dropdown', 'value'),
     Input('monthly-data-dropdown', 'value')])
def update_graph(clickData, selected_variable, selected_monthly_variable):
    if clickData is None:
        empty_figure = go.Figure()
        empty_figure.update_layout(template="plotly_white", height=400)
        return 'Choose a country', empty_figure, empty_figure
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
            height=400,
            font=dict(size=12)
        )

        fig_monthly = px.line(df_filtered_monthly, x='Date', y=selected_monthly_variable,
                              title=f'Monthly {selected_monthly_variable} in {country_name}', template="plotly_white",
                              color_discrete_sequence=['violet'])

        fig_monthly.update_layout(
            title={'text': f'Monthly {selected_monthly_variable} in {country_name}', 'x': 0.5, 'xanchor': 'center'},
            xaxis_title="Date",
            yaxis_title=selected_monthly_variable,
            height=400,
            font=dict(size=12)
        )
        return country_name, fig, fig_monthly