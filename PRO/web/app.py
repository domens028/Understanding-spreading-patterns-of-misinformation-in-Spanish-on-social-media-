from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc
import dash
import pandas as pd 
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table
import numpy as np
from pages import url,tw,languague,channels,home,topic,twitterVStelegram


app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)


# Define el contenido de la página web
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Channels", href="/Channels")),
            dbc.NavItem(dbc.NavLink("Domain", href="/url")),
            dbc.NavItem(dbc.NavLink("Languague", href="/Languague")),
            dbc.NavItem(dbc.NavLink("Twitter", href="/Twitter")),
            dbc.NavItem(dbc.NavLink("TwitterVsTelegram", href="/TwitterVsTelegram")),
            dbc.NavItem(dbc.NavLink("Topics", href="/Topic")),
        ],
        brand=dbc.NavLink("DASHBOARD", href="/"),
        color="dark",
        dark=True,
    ),
    html.Div(id='page-content',style={'margin-top': '20px'}),

])



# Define la lógica para cambiar de página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Channels':
        return channels.layout
    elif pathname == '/url':
        return url.layout
    elif pathname == '/Languague':
        return languague.layout
    elif pathname == '/Twitter':
        return tw.layout
    elif pathname == '/TwitterVsTelegram':
        return twitterVStelegram.layout
    elif pathname == '/Topic':
        return topic.layout
    else:
        return home.layout
    
home.homeCallBacks(app)
channels.ChannelCallBacks(app)
url.urlCallBacks(app)


if __name__ == '__main__':
    app.run_server()
    
    
