import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
 

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


def ObtainFigure(df,titleFigure): 
    

    #eliminamos la fila others 
    df = df.drop(df[df['channel'] == 'others'].index)
    
    #normalizamos la grafica de todo el dataset por el número de días que hay en todo el dataset
    df['ocurrences'] = (df['ocurrences'] / 99) * 100
    fig = px.bar(df, y=df['channel'], x=df['ocurrences'])
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
        'y': 0.0025,
        'x': 0.55,
        'xanchor': 'center',
        'yanchor': 'bottom'
    },
        margin=dict(t=50, b=100, l=50, r=50),# Ajustar el tamaño del margen inferior
    )
    return fig 

#ALL#
df_barCh = pd.read_csv('tables/channelallByOcurrencesPlot.csv')
figChannels = ObtainFigure(df_barCh,'MOST SHARED CHANNELS')
df_barChTo = pd.read_csv('tables/channeltodayByOcurrencesPlot.csv')
figChannelsToday = ObtainFigure(df_barChTo,'MOST SHARED CHANNELS TODAY')
df_barChWe = pd.read_csv('tables/channellastweekByOcurrencesPlot.csv')
figChannelsWeek = ObtainFigure(df_barChWe,'MOST SHARED CHANNELS LAST WEEK')
df_barChMo = pd.read_csv('tables/channellastmonthByOcurrencesPlot.csv')
figChannelsMonth = ObtainFigure(df_barChMo,'MOST SHARED CHANNELS LAST MONTH')

#SPANISH#
df_barChEs = pd.read_csv('tables/es/channelallByOcurrencesPlot.csv')
figChannelsSpanish = ObtainFigure(df_barChEs,'MOST SHARED CHANNELS')
df_barChToEs = pd.read_csv('tables/es/channeltodayByOcurrencesPlot.csv')
figChannelsTodaySpanish = ObtainFigure(df_barChToEs,'MOST SHARED CHANNELS TODAY')
df_barChWeEs = pd.read_csv('tables/es/channellastweekByOcurrencesPlot.csv')
figChannelsWeekSpanish = ObtainFigure(df_barChWeEs,'MOST SHARED CHANNELS LAST WEEK')
df_barChMoEs = pd.read_csv('tables/es/channellastmonthByOcurrencesPlot.csv')
figChannelsMonthSpanish = ObtainFigure(df_barChMoEs,'MOST SHARED CHANNELS LAST MONTH')

##ENLGISH##
df_barChEn = pd.read_csv('tables/en/channelallByOcurrencesPlot.csv')
figChannelsEnglish = ObtainFigure(df_barChEn,'MOST SHARED CHANNELS')
df_barChToEn = pd.read_csv('tables/en/channeltodayByOcurrencesPlot.csv')
figChannelsTodayEnglish = ObtainFigure(df_barChToEn,'MOST SHARED CHANNELS TODAY')
df_barChWeEn = pd.read_csv('tables/en/channellastweekByOcurrencesPlot.csv')
figChannelsWeekEnglish = ObtainFigure(df_barChWeEn,'MOST SHARED CHANNELS LAST WEEK')
df_barChMoEn = pd.read_csv('tables/en/channellastmonthByOcurrencesPlot.csv')
figChannelsMonthEnglish = ObtainFigure(df_barChMoEn,'MOST SHARED CHANNELS LAST MONTH')


opciones = [
    {'label': 'All', 'value': 'all'},
    {'label': 'Spanish', 'value': 'es'},
    {'label': 'English', 'value': 'en'},
]

layout = html.Div(children=[
        
    # All elements from the top of the page
    html.Div([
            
            dcc.Dropdown(
                id='dropbox1',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica1')
    ],style={'margin-bottom': '20px'}),
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox2',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica2')
    ],style={'margin-bottom': '20px'}),
    
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox3',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica3')
    ],style={'margin-bottom': '20px'}),
      
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox4',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica4')
    ],style={'margin-bottom': '20px'}),
])


def ChannelCallBacks(app):
    
    # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica1', 'children'),
        [dash.dependencies.Input('dropbox1', 'value')]
    )
    def actualizar_grafica1(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figChannelsEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figChannelsSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figChannels
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica2', 'children'),
        [dash.dependencies.Input('dropbox2', 'value')]
    )
    def actualizar_grafica2(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figChannelsTodayEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figChannelsTodaySpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figChannelsToday
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica3', 'children'),
        [dash.dependencies.Input('dropbox3', 'value')]
    )
    def actualizar_grafica3(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figChannelsWeekEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figChannelsWeekSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figChannelsWeek
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica4', 'children'),
        [dash.dependencies.Input('dropbox4', 'value')]
    )
    def actualizar_grafica4(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figChannelsMonthEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figChannelsMonthSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figChannelsMonth
            ),
