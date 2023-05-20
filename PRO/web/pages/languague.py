import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
 

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df_bar1 = pd.read_csv('tables/languagueallByOcurrencesPlot.csv')
#eliminamos la fila others 
df_bar1.drop(df_bar1[df_bar1['languague'] == 'others'].index,inplace=True)
#normalizamos la grafica de todo el dataset por el número de días que hay en todo el dataset
df_bar1['ocurrences'] = (df_bar1['ocurrences'] / 99) * 100
df_bar1 = df_bar1.loc[(df_bar1['ocurrences'] > 10)]
fig1 = px.bar(df_bar1, y=df_bar1['languague'], x=df_bar1['ocurrences'])
fig1.update_layout(
    autosize=False,
    height=800,
    width=1800,
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=14
    ),
    title={
        'text': "LANGUAGE IN ALL DATASET",
        'y': 0.025,
        'x': 0.55,
        'xanchor': 'center',
        'yanchor': 'bottom'
    },
    margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
)
layout = html.Div(children=[
        
    # All elements from the top of the page
    html.Div([
        html.H1(children='MOST SHARED CHANNELS ALL DATASET'),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ]),
   
])
