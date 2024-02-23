from dash import Dash, html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

meta_tags = [
    {"name": "viewport", "content": "width=device-width, inital-scale=1"}
]

app = Dash(__name__, external_stylesheets=external_stylesheets,
           meta_tags=meta_tags)


app.layout = dbc.Container(
    html.Div([
        html.H1("This is my HTML page"),
        html.Div([
            html.P("This is the first paragraph of my HTML page"),
            html.P("This is the second paragraph of my HTML page")
        ]),
        html.Div([
            html.Img(src=app.get_asset_url('bar-chart-placeholder.png'))
        ])
    ])
)

if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
