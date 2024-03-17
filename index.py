from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from components.navbar import navbar
from layouts.layout_page_1 import layout_page_1
from layouts.layout_page_2 import layout_page_2
from layouts.layout_page_3 import layout_page_3
from callbacks.callbacks_page_1 import * 
from callbacks.callbacks_page_2 import * 
from callbacks.callbacks_page_3 import * 



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return layout_page_1
    elif pathname == '/page-2':
        return layout_page_2
    elif pathname == '/page-3':
        return layout_page_3
    else:
        return "Welcome! Please choose a page."

if __name__ == '__main__':
    app.run_server(debug=True)
