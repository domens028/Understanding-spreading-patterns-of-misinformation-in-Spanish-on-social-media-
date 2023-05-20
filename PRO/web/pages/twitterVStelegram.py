import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

def ObtainFigure(df,titleFigure,tipo): 
    
    
    #normalizamos la grafica de todo el dataset por el número de días que hay en todo el dataset
    df['id'] = (df['id'] / 99) * 100
    fig = px.bar(df, y=df[tipo], x=df['id'])
    #creamos la figura a nuestro gusto 
    fig.update_layout(
        autosize=False,
        height=1000,
        width=1600,
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=20
        ),  
        title={
        'text': titleFigure,
        'y': 0.025,
        'x': 0.55,
        'xanchor': 'center',
        'yanchor': 'bottom'
    },
        margin=dict(t=50, b=100, l=50, r=50),# Ajustar el tamaño del margen inferior
    )
    return fig 

df_bar5 = pd.read_csv('tables/TwitterToTelegram.csv')
df_bar6 = pd.read_csv('tables/TelegramToTwitter.csv')
df_bar7 = pd.read_csv('tables/ChannelsTelegramToTwitter.csv')
df_bar8 = pd.read_csv('tables/ChannelsTwitterToTelegram.csv')



layout = html.Div(children=[
    html.Div([
            
            dcc.Graph(
                figure=ObtainFigure(df_bar5, 'SHARED DOMAINS IN TWITTER BEFORE TELEGRAM','url')
            ),
    ],style={'margin-bottom': '20px'}),
        
    # All elements from the top of the page
    html.Div([
            
            dcc.Graph(
                figure=ObtainFigure(df_bar6, 'SHARED DOMAINS IN TELEGRAM BEFORE TWITTER','url')
            ),
    ],style={'margin-bottom': '20px'}),
    
      # All elements from the top of the page
    html.Div([
            
            dcc.Graph(
                figure=ObtainFigure(df_bar7, 'SHARED CHANNELS IN TELEGRAM BEFORE TWITTER','channel')
            ),
    ],style={'margin-bottom': '20px'}),
    
      # All elements from the top of the page
    html.Div([
            
            dcc.Graph(
                    figure=ObtainFigure(df_bar8, 'SHARED CHANNELS IN TWITTER BEFORE TELEGRAM','channel')
            ),
    ],style={'margin-bottom': '20px'}),
    
             
             
])