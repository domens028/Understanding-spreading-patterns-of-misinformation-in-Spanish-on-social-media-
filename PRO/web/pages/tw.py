import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
 




# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df_bar1 = pd.read_csv('tables/RetweetPerDomain.csv')

df_bar1['retweet'] = (df_bar1['retweet'] / 99) * 100
df_bar1 = df_bar1.loc[(df_bar1['retweet'] > 1000)]
fig1 = px.bar(df_bar1, y=df_bar1['url'], x=df_bar1['retweet'])

#creamos la figura a nuestro gusto 
fig1.update_layout(
    autosize=False,
    height=700,
    width=1600,
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=20
    ),
    #title={
    #    'text': "RETWEET PER DOMAIN IN ALL DATASET",
    #    'y': 0.025,
    #    'x': 0.55,
    #    'xanchor': 'center',
    #    'yanchor': 'bottom'
    #},
    margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
)

df_bar2 = pd.read_csv('tables/LikePerDomian.csv')
df_bar2['favorites'] = (df_bar2['favorites'] / 99) * 100
df_bar2 = df_bar2.loc[(df_bar2['favorites'] > 11000)]

fig2 = px.bar(df_bar2, y=df_bar2['url'], x=df_bar2['favorites'])
fig2.update_layout(
    autosize=False,
    height=700,
    width=1600,
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=20
    ),
    margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
)

df_bar3 = pd.read_csv('tables/RetweetPerChannel.csv')
df_bar3['retweet'] = (df_bar3['retweet'] / 99) * 100
df_bar3 = df_bar3.loc[(df_bar3['retweet'] > 5000)]
fig3 = px.bar(df_bar3, y=df_bar3['channel'], x=df_bar3['retweet'])
fig3.update_layout(
    autosize=False,
    height=700,
    width=1600,
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=20
    ),
   
    margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
)
df_bar4 = pd.read_csv('tables/LikePerChannel.csv')
df_bar4['favorites'] = (df_bar4['favorites'] / 99) * 100
df_bar4 = df_bar4.loc[(df_bar4['favorites'] > 11000)]
fig4 = px.bar(df_bar4, y=df_bar4['channel'], x=df_bar4['favorites'])
fig4.update_layout(
    autosize=False,
    height=700,
    width=1600,
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=20
    ),
   
    margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
)
layout = html.Div(children=[
        
    # All elements from the top of the page
    html.Div([
        html.H1(children='RETWEET PER DOMAIN IN ALL DATASET'),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='LIKES PER DOMAIN IN ALL DATASET'),
        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
    
      html.Div([
        html.H1(children='RETWEET PER CHANNEL IN ALL DATASET'),


        dcc.Graph(
            id='graph3',
            figure=fig3
        ),  
    ]),
      
        html.Div([
        html.H1(children='LIKE PER CHANNEL IN ALL DATASET'),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),
])
