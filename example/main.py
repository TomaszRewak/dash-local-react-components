from dash import Dash, html, callback, Input, Output, State
from dash_local_react_components import load_react_component

app = Dash(__name__)

MyComponent = load_react_component(app, 'react_components', 'my_component.js')

app.layout = html.Div([
    html.H1('My custom component test'),
    MyComponent(id='my-component', count=10),
    html.Button(id='my-button', children='save')
])


@callback(
    Output('my-button', 'children'),
    Input('my-button', 'n_clicks'),
    State('my-component', 'count'),
    prevent_initial_call=True
)
def on_click(n_clicks, count):
    return f'saved {count}'


app.run_server(debug=True)
