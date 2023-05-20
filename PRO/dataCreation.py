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


#Convert the json no_active data into dataFrames
def createDataFrameForAnalisis(jsonfile):
    channel = []
    twitter = []
    url = []
    date = []
    title = []
    text = []
    languague = []
    with open(jsonfile, encoding='utf8') as file:
        data = json.load(file)

    df = pd.DataFrame.from_dict(data, orient='columns')
    df.drop(['_index','_type','_score'], axis = 'columns', inplace=True)
    if ('old' in jsonfile):
        for index,row in df.iterrows():
            channel.append(row['_source']['doc']['channel'])
            date.append(row['_source']['doc']['date'])
            url.append(urlparse(row['_source']['doc']['url']).netloc)
            title.append(row['_source']['doc']['title']) 
           
            if(row['_source']['doc']['text']):
                 text.append(row['_source']['doc']['text'])  
                 languague.append(detect(row['_source']['doc']['text']))
            else:
                text.append(row['_source']['doc']['text'])  
                languague.append(0)
                
            if(row['_source']['doc']['twitter']):
                twitter.append(row['_source']['doc']['twitter'])
            else:
                twitter.append("no_data")
    else:
        for index,row in df.iterrows():
            channel.append(row['_source']['channel'])
            date.append(row['_source']['date'])
            url.append(urlparse(row['_source']['url']).netloc)
            title.append(row['_source']['title']) 
            if(row['_source']['text']):
                 text.append(row['_source']['text'])  
                 languague.append(detect(row['_source']['text']))
            else:
                text.append(row['_source']['text'])  
                languague.append(0)
                
            if(row['_source']['twitter']):
                twitter.append(row['_source']['twitter'])
            else:
                twitter.append("no_data")
            
    df['channel'] = channel
    df['twitter'] = twitter
    df['title'] = title
    df['url'] = url
    df['date'] = date
    df['text'] = text
    df['languague'] = languague
    #eliminamos twitter porq ahora mismo no nos interesa 
    df.drop(['_source'], axis = 'columns', inplace=True)
    df.rename(columns = {'_id':'id'}, inplace = True)
    return df 


def channelTransformation(data):
    channelDf = pd.DataFrame()
    for index,row in data.iterrows():
            for clave in row['channel'].keys():
                    newLine = {}
                    newLine['id'] = row['id']
                    newLine['channel'] = clave
                    channelDf = channelDf.append(newLine, ignore_index=True)
    return channelDf

def hostNameTranformation(data):
     for index,row in data.iterrows():
        host = row['url']
        if(not (host.startswith('www.'))):
                row['url'] = 'www.' + host
                            
     return data

def twitterTranformation(df):
    twitterDf = pd.DataFrame()
    for index,row in df.iterrows():
        try:
            for clave in row['twitter'].keys():
                    newLine = {}
                    newLine['id'] = row['id']
                    newLine['TwitterId'] = clave
                    newLine['TwitterText'] = row['twitter'][clave]['text']
                    newLine['retweet'] = row['twitter'][clave]['retweet']
                    newLine['name'] = row['twitter'][clave]['name']
                    newLine['favorites'] = row['twitter'][clave]['favorites']
                    newLine['quoted_tweets'] = row['twitter'][clave]['quoted_tweets']
                    
                    
                    twitterDf = twitterDf.append(newLine, ignore_index=True)      
        except:
            print(row['twitter'])
            
    return twitterDf   
                 
def quaoted_tweets(df):
    for index,row in df.iterrows():
          
            for clave in row['quoted_tweets'].keys():
                if(clave!="{}"):
                    newLine = {}
                    newLine['id'] = row['id']
                    newLine['TwitterId'] = clave
                    newLine['TwitterText'] = row['quoted_tweets'][clave]['text']
                    newLine['retweet'] = row['quoted_tweets'][clave]['retweet']
                    newLine['favorites'] = row['quoted_tweets'][clave]['favorites']
                    newLine['quoted_tweets'] = 'yes'
                    df = df.append(newLine, ignore_index=True)  
        
              
    return df  

def CreateData():
    #Obtain the Active data 
    dataActive = createDataFrameForAnalisis('Datasheets/07-Dec/2022-12-07_data.json')
    #obtain the no_active data
    dataNoActive = createDataFrameForAnalisis('Datasheets/07-Dec/2022-12-07_old_data.json')
    data1= pd.concat([dataActive, dataNoActive], axis=0)
    data1 = data1.drop_duplicates(subset = ['id'],
                            keep='first')

    #Obtain the Active data 
    dataActive = createDataFrameForAnalisis('Datasheets/08-Feb/2023-02-08_data.json')
    #obtain the no_active data
    dataNoActive = createDataFrameForAnalisis('Datasheets/08-Feb/2023-02-08_old_data.json')
    #we concat the two datasets in one called data
    data2= pd.concat([dataActive, dataNoActive], axis=0)
    data2 = data2.drop_duplicates(subset = ['id'],
                            keep='first')

    data= pd.concat([data1, data2], axis=0)
    #We transofrm the channel data 
    twitterDf = twitterTranformation(data)
    twitterDf = quaoted_tweets(twitterDf)
    channelDf = channelTransformation(data)       
    data.drop(['channel'], axis = 'columns', inplace=True)
    #Merge both datasets the one with the channel transformation and the one with the complete dataset 
    data = pd.merge(channelDf, data, how="inner", on=["id", "id"])
    data = pd.merge(data, twitterDf, how="left", on=["id", "id"])
    data = hostNameTranformation(data)

    data.to_csv("data.csv")
    return data
