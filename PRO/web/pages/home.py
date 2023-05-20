from dash import Dash, html, dcc, callback
import dash_bootstrap_components as dbc
import dash
import pandas as pd 
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dash_table
import numpy as np



df = pd.read_csv('data_clean.csv')
#Delete the columns that we don´t need 
table = df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'title',
       'text', 'TwitterId', 'TwitterText','twitter',   
       'quoted_tweets'], axis = 'columns')


df_bar1 = pd.read_csv('tables/channelallByOcurrencesPlot.csv')
#eliminamos la fila others 
df_bar1.drop(0, inplace=True)
#normalizamos la grafica de todo el dataset por el número de días que hay en todo el dataset
df_bar1['ocurrences'] = (df_bar1['ocurrences'] / 99) * 100
fig1 = px.bar(df_bar1, y=df_bar1['channel'], x=df_bar1['ocurrences'])


df_bar2 = pd.read_csv('tables/urlallByOcurrencesPlot.csv')
df_bar2.drop(154, inplace=True)
df_bar2 = df_bar2.loc[(df_bar2['ocurrences'] > 50)]
df_bar2['ocurrences'] = (df_bar2['ocurrences'] / 99) * 100
fig2 = px.bar(df_bar2, y=df_bar2['url'], x=df_bar2['ocurrences'])




df = df.assign(Telegram = np.where((df.TwitterId > 0),'Twitter','Telegram'))
df = df.assign(PieId = 1)

df2 = df.loc[(df['TwitterId'] > 0)]
df2= df2.assign(antes = np.where((df2.date >= df2.TwitterDate),'Twitter','Telegram'))

fig3 = px.pie(df,values='PieId',names='Telegram',width=350,height=350)
fig3.update_layout(
 title={
        'text': "NEWS",
     
    },
 )
fig4 = px.pie(df2,values='PieId',names='antes',width=350,height=350)
fig4.update_layout(
 title={
        'text': "TWITTER BEFORE TELEGRAM",
    },
 )

# Definir las opciones del Dropbox
opciones = [
    {'label': 'MOST SHARED CHANNELS', 'value': 'Channels'},
    {'label': 'MOST SHARED DOMAINS', 'value': 'Domain'},
]


layout = dbc.Container([ 
        
    
        html.Div([
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id='graph1',
                        figure=fig3
                    ),
                    width=3
                ),
                dbc.Col(
                    dcc.Graph(
                        id='graph2',
                        figure=fig4
                    ),
                    width=3
                ),
                dbc.Col(
                    html.Div([
                        dcc.Dropdown(
                            id='dropbox',
                            options=opciones,
                            value=opciones[0]['value']  # Valor inicial seleccionado
                        ),
                        html.Div(id='contenido-grafica')
                    ]),
                    width=6
                )
     
        ]),
        
            dbc.Row([
                
                dash_table.DataTable(
                id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "selectable": True} for i in df.columns
                ],
                data=table.to_dict('records'),
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                page_size= 10,
                ),
                    
            
            ])
        ], style={'margin-top': '20px'})
    ],
    fluid=True
)

def homeCallBacks(app):
    
    # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica', 'children'),
        [dash.dependencies.Input('dropbox', 'value')]
    )
 
    def actualizar_grafica(opcion):
        
        if opcion == 'Channels':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=fig1
                        ),
        elif opcion == 'Domain':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = fig2
            )    