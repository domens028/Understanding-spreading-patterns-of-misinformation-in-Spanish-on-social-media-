import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


opciones = [
    {'label': 'All', 'value': 'all'},
    {'label': 'Spanish', 'value': 'es'},
    {'label': 'English', 'value': 'en'},
]

def ObtainFigure(df,titleFigure): 
    
    #eliminamos la fila others 
    df = df.drop(df[df['url'] == 'others'].index)
    #normalizamos la grafica de todo el dataset por el número de días que hay en todo el dataset
    df['ocurrences'] = (df['ocurrences'] / 99) * 100
    fig = px.bar(df, y=df['url'], x=df['ocurrences'])
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
        margin=dict(t=50, b=100, l=50, r=50) # Ajustar el tamaño del margen inferior
    )
    return fig 


#ALL#
df_barUrl = pd.read_csv('tables/urlallByOcurrencesPlot.csv')
figDomain = ObtainFigure(df_barUrl,'MOST SHARED DOMAIN')
df_barUrlTo = pd.read_csv('tables/urltodayByOcurrencesPlot.csv')
figDomainToday = ObtainFigure(df_barUrlTo,'MOST SHARED Domain TODAY')
df_barUrlWe = pd.read_csv('tables/urllastweekByOcurrencesPlot.csv')
figDomainWeek = ObtainFigure(df_barUrlWe,'MOST SHARED Domain LAST WEEK')
df_barUrlMo = pd.read_csv('tables/urllastmonthByOcurrencesPlot.csv')
figDomainMonth = ObtainFigure(df_barUrlMo,'MOST SHARED Domain LAST MONTH')

#SPANISH#
df_barUrlEs = pd.read_csv('tables/es/urlallByOcurrencesPlot.csv')
figDomainSpanish = ObtainFigure(df_barUrlEs,'MOST SHARED DOMAIN')
df_barUrlToEs = pd.read_csv('tables/es/urltodayByOcurrencesPlot.csv')
figDomainTodaySpanish = ObtainFigure(df_barUrlToEs,'MOST SHARED DOMAIN TODAY')
df_barUrlWeEs = pd.read_csv('tables/es/urllastweekByOcurrencesPlot.csv')
figDomainWeekSpanish = ObtainFigure(df_barUrlWeEs,'MOST SHARED DOMAIN LAST WEEK')
df_barUrlMoEs = pd.read_csv('tables/es/urllastmonthByOcurrencesPlot.csv')
figDomainMonthSpanish = ObtainFigure(df_barUrlMoEs,'MOST SHARED DOMAIN LAST MONTH')

##ENLGISH##
df_barUrlEn = pd.read_csv('tables/en/urlallByOcurrencesPlot.csv')
figDomainEnglish = ObtainFigure(df_barUrlEn,'MOST SHARED DOMAIN')
df_barUrlToEn = pd.read_csv('tables/en/urltodayByOcurrencesPlot.csv')
figDomainTodayEnglish = ObtainFigure(df_barUrlToEn,'MOST SHARED DOMAIN TODAY')
df_barUrlWeEn = pd.read_csv('tables/en/urllastweekByOcurrencesPlot.csv')
figDomainWeekEnglish = ObtainFigure(df_barUrlWeEn,'MOST SHARED DOMAIN LAST WEEK')
df_barUrlMoEn = pd.read_csv('tables/en/urllastmonthByOcurrencesPlot.csv')
figDomainMonthEnglish = ObtainFigure(df_barUrlMoEn,'MOST SHARED DOMAIN LAST MONTH')


layout = html.Div(children=[
        
    # All elements from the top of the page
    html.Div([
            
            dcc.Dropdown(
                id='dropbox5',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica5')
            
    ],style={'margin-bottom': '20px'}),
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox6',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica6')
    ],style={'margin-bottom': '20px'}),
    
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox7',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica7')
    ],style={'margin-bottom': '20px'}),
      
    # All elements from the top of the page
     html.Div([
            dcc.Dropdown(
                id='dropbox8',
                options=opciones,
                value=opciones[0]['value']  # Valor inicial seleccionado
            ),
            html.Div(id='contenido-grafica8')
    ],style={'margin-bottom': '20px'}),
])


def urlCallBacks(app):
    
    # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica5', 'children'),
        [dash.dependencies.Input('dropbox5', 'value')]
    )
    def actualizar_grafica5(opcion):

        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figDomainEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figDomainSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figDomain
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica6', 'children'),
        [dash.dependencies.Input('dropbox6', 'value')]
    )
    def actualizar_grafica6(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figDomainTodayEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figDomainTodaySpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figDomainToday
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica7', 'children'),
        [dash.dependencies.Input('dropbox7', 'value')]
    )
    def actualizar_grafica7(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figDomainWeekEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figDomainWeekSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figDomainWeek
            ),
     # Definir la función de actualización de contenido
    @app.callback(
        dash.dependencies.Output('contenido-grafica8', 'children'),
        [dash.dependencies.Input('dropbox8', 'value')]
    )
    def actualizar_grafica8(opcion):
        if opcion == 'en':
            # Aquí puedes agregar el código para la gráfica 1
            return   dcc.Graph(
                            figure=figDomainMonthEnglish
                        ),
        elif opcion == 'es':
            # Aquí puedes agregar el código para la gráfica 2
            return dcc.Graph(
                figure = figDomainMonthSpanish
            ),
        elif opcion == 'all':   
              return dcc.Graph(
                figure = figDomainMonth
            ),

