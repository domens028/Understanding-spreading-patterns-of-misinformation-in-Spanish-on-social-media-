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
import datetime
import os 

def group(name,date,data):
    table = data.groupby([name])['id'].count()
    df = table.to_frame().reset_index()
    df.rename(columns = {'id':'ocurrences'}, inplace = True)
    if(date != 'today'):
        others = df[df.ocurrences < 10]
        df=df.drop(others.index)
        df=df.append({name:'others','ocurrences':others.count().ocurrences},ignore_index=True)
    return df

def groupBy(name,date,data):
    df = group(name,date,data)
    df = df.sort_values('ocurrences', ascending=True)
    df.to_csv('tables/'+name+date+'ByOcurrencesPlot.csv',index=False) 

def languagueGroupBy(name,date,data,languague):
    df = group(name,date,data)
    df = df.sort_values('ocurrences', ascending=True)
    df.to_csv('tables/'+languague+'/'+name+date+'ByOcurrencesPlot.csv',index=False) 
    

def ChannelPerPost(data):#Número de Canales que se comparten por post
    table = data.groupby(['channel'])['id'].count()
    df= table.to_frame().reset_index()
    return df

def DomainsPerPost(data):#Número de dominios compartidos por post
    table = data.groupby(['url'])['id'].count()
    df= table.to_frame().reset_index()
    return df

def PostPerTwitter(data):#Número de veces que un post se comparte en telegram y acaba en twitter
    table = data.groupby(['id','date'])['TwitterId'].count()
    df = table.to_frame().reset_index()
    return df

def DomainsPerTwitter(data):#Número de veces que un dominio se comparte en telegram y acaba en twitter
    table = data.groupby(['url','date'])['TwitterId'].count()
    df = table.to_frame().reset_index()
    return df


def RetweetPerDomain(data):#Numero de retweet en función del dominio
    table = data.groupby(['url'])['retweet'].sum()
    df = table.to_frame().reset_index()
    df = df.sort_values('retweet', ascending=True)
    df.to_csv('tables/RetweetPerDomain.csv',index=False) 
    return df

def LikesPerDomain(data):#Numero de me gustas en función del dominio
    table = data.groupby(['url'])['favorites'].sum()
    df = table.to_frame().reset_index()
    df = df.sort_values('favorites', ascending=True)
    df.to_csv('tables/LikePerDomian.csv',index=False) 
    return df

def RetweetPerChannel(data):#Numero de retweet en función del dominio
    table = data.groupby(['channel'])['retweet'].sum()
    df = table.to_frame().reset_index()
    df = df.sort_values('retweet', ascending=True)
    df.to_csv('tables/RetweetPerChannel.csv',index=False) 
    return df

def LikesPerChannel(data):#Numero de me gustas en función del dominio
    table = data.groupby(['channel'])['favorites'].sum()
    df = table.to_frame().reset_index()
    df = df.sort_values('favorites', ascending=True)
    df.to_csv('tables/LikePerChannel.csv',index=False) 
    return df




def AnalisisDeDireccionabilidad(data):
    #Analisis de direccionabilidad 
    #cogemos solo los datos con tweets 
    df = data.loc[(data['TwitterId'] > 0)]
    df = df.assign(antes = np.where((df.date >= df.TwitterDate),'Twitter','Telegram'))
    print(df.loc[:, ['date', 'TwitterDate','antes']])
    print(df.antes.value_counts())
    
    #Telegram to Twitter
    df2 = df.loc[(df['antes'] == 'Telegram')]
    dmxps = DomainsPerPost(df2)
    chxps = ChannelPerPost(df2)
    dmxps = dmxps.sort_values('id', ascending=True)
    chxps = chxps.sort_values('id', ascending=True)
    dmxps.to_csv('tables/TelegramToTwitter.csv',index=False) 
    chxps.to_csv('tables/ChannelsTelegramToTwitter.csv',index=False) 
    #Twitter to Telegram
    df2 = df.loc[(df['antes'] == 'Twitter')]
    dmxps = DomainsPerPost(df2)
    chxps = ChannelPerPost(df2)
    dmxps = dmxps.sort_values('id', ascending=True)
    chxps = chxps.sort_values('id', ascending=True)
    dmxps.to_csv('tables/TwitterToTelegram.csv',index=False) 
    chxps.to_csv('tables/ChannelsTwitterToTelegram.csv',index=False) 

def TwitterAnalisis(data):
    #DOMINIOS 
    rtxdm = RetweetPerDomain(data)
    lkxdm = LikesPerDomain(data)
    #CHANNELS 
    rtxch = RetweetPerChannel(data)
    lkxch = LikesPerChannel(data)
    

def printTables(data):
    #Date of analisis 

    fecha = datetime.datetime(2023, 2, 8)

    today = data.loc[(data['date'] == fecha)]

    groupBy('url','today',today)
    groupBy('channel','today',today)
    groupBy('languague','today',today)

    #lastWeek
    filterDate = fecha - timedelta(days=7)
    lastweek = data.loc[(data['date'] >= filterDate)
                        & (data['date'] < fecha)]
    groupBy('url','lastweek',lastweek)
    groupBy('channel','lastweek',lastweek)
    groupBy('languague','lastweek',lastweek)

    #lastMonth
    filterDate = fecha - timedelta(days=30)
    lastmonth = data.loc[(data['date'] >= filterDate)
                        & (data['date'] < fecha)]

    groupBy('url','lastmonth',lastmonth)
    groupBy('channel','lastmonth',lastmonth)
    groupBy('languague','lastmonth',lastmonth)
    #allDataSet
    groupBy('url','all',data)
    groupBy('channel','all',data)
    groupBy('languague','all',data)

    
    
def printTablesLan(data):
    lan = ['es','en']
    path = os.getcwd() 
    fecha = datetime.datetime(2023, 2, 8)
    for x in lan:
        #We create the folders for the tables
        try:
                os.mkdir(path+'/tables/'+str(x))
        except OSError as error:
                error
                
        #We filter by  languague 
        df = data.loc[(data['languague'] == x)]
        #We filter by the date

        today = df.loc[(df['date'] == fecha)]
        languagueGroupBy('url','today',today,str(x))
        languagueGroupBy('channel','today',today,str(x))
        #lastWeek
        filterDate = fecha - timedelta(days=7)
        lastweek = df.loc[(df['date'] >= filterDate)
                            & (df['date'] < fecha)]
        languagueGroupBy('url','lastweek',lastweek,str(x))
        languagueGroupBy('channel','lastweek',lastweek,str(x))
        
        #lastMonth
        filterDate = fecha - timedelta(days=30)
        lastmonth = df.loc[(df['date'] >= filterDate)
                            & (df['date'] < fecha)]

        languagueGroupBy('url','lastmonth',lastmonth,str(x))
        languagueGroupBy('channel','lastmonth',lastmonth,str(x))

        #allDataSet
        languagueGroupBy('url','all',df,str(x))
        languagueGroupBy('channel','all',df,str(x))