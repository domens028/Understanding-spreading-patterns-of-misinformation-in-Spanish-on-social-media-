import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from dash import dash_table
import base64


imagen_path = 'grafo_optimizado.png'  # Reemplaza con la ruta de tu carpeta de imágenes
df = pd.read_csv('bertopicResults.csv')

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
        
        dcc.Graph(
        figure=visualizarModelo())
        
    ]),
    
    html.Button("Cargar imagen", id="boton-cargar"),
    html.Img(id='imagen'),
 
    
    
    html.Div([
        
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
                page_size= 10,
                ),
        
    ])
    
 
])



def TopiCallBack(app):
    @app.callback(
        dash.dependencies.Output('imagen', 'src'),
        [Input('boton-cargar', 'n_clicks')]
    )
    def mostrar_imagen(n_clicks):
        if n_clicks:
            imagen_bytes = cargar_imagen(imagen_path)
            return 'data:image/png;base64,{}'.format(base64.b64encode(imagen_bytes).decode())
        else:
            return dash.no_update