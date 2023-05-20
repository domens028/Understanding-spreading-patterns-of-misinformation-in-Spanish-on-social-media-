import pandas as pd
import numpy as np
import json
from pandas import json_normalize
from dash import Dash, html, dcc
import plotly.express as px
from urllib.parse import urlparse
from langdetect import detect
from datetime import date
from datetime import timedelta

def clean(data):
    #Limpiamos la base de datos, tras observar que hay campos que tienen el title=='NEWS? y el text =='NULL'
    data= data.drop(data[(data['twitter'] =='no_data') & (data['title'] =='NEWS') & (data['text'].isnull())].index)
    pr = data[~data['text'].str.contains('JavaScript', na = False)]
    data= data.drop(data[data['text'].str.contains('JavaScript', na = False)].index)
    data = data.replace({'TwitterDate': {'no_data': 0}})
    #Le quitamos los segundos a las fechas
    data['date_ms'] = data['date']
    data['date'] = data['date'].str.slice(stop=10)
    data['TwitterDate'] = data['TwitterDate'].str.slice(stop=10)
    #Los convertimos en date con el formato  yyyy-mm-dd
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['TwitterDate'] = pd.to_datetime(data['TwitterDate'], format='%Y-%m-%d')
    #Completamos con los campos text vacios 
    data = data.fillna({'text': data.TwitterText})#completamos con twitter siempre que se pueda
    data = data.fillna({'text': data.title})#completamos con title cuando no se pueda con twitter
    #Corregimos el lenguaje 
    languague = []
    for index,row in data.iterrows():
        try:
            languague.append(detect(row['text']))
        except:
            languague.append(0)
       
    data['languague'] = languague       
    print(data.count())
    data.to_csv('data_clean.csv')
    return data