import pandas as pd
import numpy as np
import json
from pandas import json_normalize
import plotly.express as px
from urllib.parse import urlparse
from langdetect import detect
from datetime import date
from datetime import timedelta
from bertopic import BERTopic
from bertopic.vectorizers import ClassTfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def analisis():
    df = pd.read_csv('data_clean.csv')
    #Filtramos por idioma español 
    pr = df.loc[(df['languague'] == 'es')]
    pr.reset_index(inplace=True, drop=True)
    #Pasamos el campo texto 
    docs = pr['text']
    print(docs.count())

    #Ejecutamos el modelo 
    print('Comienza la ejecución del modelo')
    ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
    topic_model = BERTopic(ctfidf_model=ctfidf_model, nr_topics=100 ,calculate_probabilities=True, verbose=True)
    topics, probs = topic_model.fit_transform(docs)
    topic_model.save("BertopicModel1")
    output = topic_model.get_topic_info()
    output.to_csv('tables/pages/bertopicResults.csv')
    
    print('Acaba la ejecución del modelo')

