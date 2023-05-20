import configparser

def credentails_twitter(config_file):
    """
    Reads the data from config file and makes the authentification
    in twitter api

    Parameters:
        config_file -> configuration file
    
    Return:
        Dictionary with data from file
    """
        

    config_list = list()
    # Reading Configs
    config = configparser.ConfigParser()
    config.read(config_file)

    # Read credentials from file
    CONSUMER_KEY = config['Twitter']['CONSUMER_KEY']
    CONSUMER_SECRET = config['Twitter']['CONSUMER_SECRET']
    ACCESS_TOKEN = config['Twitter']['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = config['Twitter']['ACCESS_TOKEN_SECRET']
    
    config_list.append({'CONSUMER_KEY': CONSUMER_KEY, 'CONSUMER_SECRET': CONSUMER_SECRET, 'ACCESS_TOKEN' : ACCESS_TOKEN, 'ACCESS_TOKEN_SECRET': ACCESS_TOKEN_SECRET})
    
    # Read credentials from file
    CONSUMER_KEY = config['Twitter1']['CONSUMER_KEY']
    CONSUMER_SECRET = config['Twitter1']['CONSUMER_SECRET']
    ACCESS_TOKEN = config['Twitter1']['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = config['Twitter1']['ACCESS_TOKEN_SECRET']
    
    config_list.append({'CONSUMER_KEY': CONSUMER_KEY, 'CONSUMER_SECRET': CONSUMER_SECRET, 'ACCESS_TOKEN' : ACCESS_TOKEN, 'ACCESS_TOKEN_SECRET': ACCESS_TOKEN_SECRET})
   
    return config_list