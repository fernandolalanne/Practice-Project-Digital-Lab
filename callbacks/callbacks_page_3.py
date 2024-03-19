from dash.dependencies import Input, Output, State
from app import app
import plotly.express as px
import plotly.graph_objects as go
from load_data import df_concatenado, df_covid_combined
from layouts.layout_page_3 import df_covid_selected, df_economic_selected


def generate_3d_correlation_graph(df, vars):
    # Asegúrate de que sólo se seleccionen las variables válidas
    df = df[vars].dropna()
    
    if len(vars) < 3:
        print("You need at least 3 variables.")
        return go.Figure()
    
    # Calcular la matriz de correlación
    corr_matrix = df.corr()
    
    # Preparar datos para el gráfico 3D
    x_data, y_data, z_data = [], [], []
    for i, var1 in enumerate(vars):
        for j, var2 in enumerate(vars):
            if i != j:  # Evitar comparar una variable consigo misma
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
            color=z_data,  # Color de los puntos por valor de correlación
            colorscale='Viridis',  # Escala de colores
            opacity=0.8,
            colorbar=dict(title='Correlation'),  # Personaliza la barra de color
        ),
        text=[f'{x}, {y}: {z:.2f}' for x, y, z in zip(x_data, y_data, z_data)],  # Texto mostrado al pasar el cursor sobre los puntos
    )])
    
    # Configuración del layout del gráfico
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), scene=dict(
                      xaxis_title='Variable X',
                      yaxis_title='Variable Y',
                      zaxis_title='Correlación'))
    return fig


@app.callback(
    [Output('selected-country-graph', 'figure'),
     Output('economic-bubble-chart', 'figure'),
     Output('covid-evolution-graph', 'figure'),
     Output('economic-evolution-graph', 'figure'),
     Output('covid-correlation-3d', 'figure'),
     Output('economic-correlation-3d', 'figure')],
    [Input('country-dropdown-page3', 'value'),
     Input('covid-vars-dropdown', 'value'),
     Input('economic-vars-dropdown', 'value')]
)

def update_selected_country_graph(selected_country, selected_covid_vars, selected_economic_vars):
    filtered_df = df_economic_selected[df_economic_selected['Entity'] == selected_country]
    fig = px.bar(filtered_df, x='Year', y=['GDP', 'Money spent in the education area','Gini Coefficient'], title=f'Data for {selected_country}')

    fig2 = px.scatter(filtered_df, 
                     x='Year', 
                     y='GDP', 
                     size='Gini Coefficient',  # Asume que GINI es una columna en tu df
                     color='Money spent in the education area',  # Usando Educación como color
                     hover_name='Entity', 
                     title=f'Economic Bubble Chart for {selected_country} over Time',
                     size_max=60)  # Máximo tamaño de burbuja
    
    fig2.update_layout(transition_duration=500)

    filtered_covid_df = df_covid_combined[df_covid_combined['location'] == selected_country][selected_covid_vars]
    filtered_economic_df = df_concatenado[df_concatenado['Entity'] == selected_country][selected_economic_vars]
    
    # Genera los gráficos 3D basados en las variables seleccionadas
    fig5 = generate_3d_correlation_graph(filtered_covid_df, selected_covid_vars)
    fig6 = generate_3d_correlation_graph(filtered_economic_df, selected_economic_vars)
    
    fig3 = px.line(df_covid_selected, x='Date', y='Total cases per million', color='location', title='COVID-19 Total Cases Evolution for Selected Countries')
    fig4 = px.area(df_economic_selected, x='Year', y='GDP', color='Entity', line_group='Entity', title='GDP Evolution for Selected Countries')

    return fig, fig2, fig3, fig4, fig5, fig6