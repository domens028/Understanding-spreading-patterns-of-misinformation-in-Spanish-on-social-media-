import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from dash import dash_table
import base64
import dash_bootstrap_components as dbc

imagen_path = 'grafo_optimizado.png'  # Reemplaza con la ruta de tu carpeta de imágenes
df = pd.read_csv('bertopicResults.csv')
df_graph = pd.read_csv('GraphNodes.csv')

def cargar_imagen(imagen_path):
    with open(imagen_path, 'rb') as file:
        imagen_bytes = file.read()
    return imagen_bytes


def visualizarModelo():
    topic_model = BERTopic.load("BertopicModel1")
    return topic_model.visualize_topics()

imagen_bytes = cargar_imagen(imagen_path)

layout = html.Div(children=[
    
    
      html.Div([
            dbc.Row([
                dbc.Col(
                      
                    dcc.Graph(
                    figure=visualizarModelo()
                    ),
                    width=6
                ),
                dbc.Col(
                    
                      
                    dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "selectable": True} for i in df.columns
                            ],
                          
                            data=df.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode="multi",
                            page_action="native",
                            page_current= 0,
                            page_size= 20,
                            ),
                                
                                width=6
                            ),
                
        ]),
            
               dbc.Row([
                dbc.Col(
                      
                  
                    html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(imagen_bytes).decode()),style={'width': '75%', 'height': '75%'}),
                    width=6
                ),
                
                
                dbc.Col(
                      
                dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "selectable": True} for i in df_graph.columns
                            ],
                          
                            data=df_graph.to_dict('records'),
                            sort_action="native",
                            sort_mode="multi",
                            page_action="native",
                            page_current= 0,
                            page_size= 20,
                            ),
                                
                                width=6
                            ),
                
        ]),
            
                
        ]),

])

