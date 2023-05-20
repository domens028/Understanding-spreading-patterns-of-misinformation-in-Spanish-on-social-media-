import tweepy
import json
from datetime import timedelta, datetime
import time
import sys
import argparse
import logging
import pandas as pd 
import random 
import numpy as np
from twitter import configuration as cf



def auth(config_file):
    """
    Reads the data o the configutation file to obain the authentification
    in twitter api

    Parameters:
        config_file -> configuration file

    Returns:
        Twitter Client API
    """

    twitter_data = cf.credentails_twitter(config_file)

    api_list = list()

    for data in twitter_data:

        try:
            # Authentification
            auth = tweepy.OAuthHandler(
                data['CONSUMER_KEY'], data['CONSUMER_SECRET'])
            auth.set_access_token(
                data['ACCESS_TOKEN'], data['ACCESS_TOKEN_SECRET'])
            
        
            api = tweepy.API(auth)

            api_list.append(api)
        except:
            logging.error("Error in Twitter when auth")
        

    return api_list[0], api_list[0]


def get_api():
    api1, api2 = auth('twitter/config.ini')
    
    if random.randint(1, 2) == 1:
        return api1
    else:
        return api2



def search_tweets(api, id):
    """
    Gets the tweets that contain a specific url

    Parameters:
        api ->  Twitter API
        query ->  query with url to find in twitter

    Returns:
        Tweets conaining the url
    """
    try:
        tweets_search  = api.get_status(id)
        return tweets_search.created_at
    except:
        logging.warn('Error')
        return 'no_data'
   
def search_tweets_text(api, id):
    """
    Gets the tweets that contain a specific url

    Parameters:
        api ->  Twitter API
        query ->  query with url to find in twitter

    Returns:
        Tweets conaining the url
    """
    try:
        tweets_search  = api.get_status(id)
        return tweets_search.text
    except:
        logging.warn('Error')
        return 'no_data'

