import re
import requests 
from datetime import date



data = "http://144.76.187.187:8001/all_data"
old_data = "http://144.76.187.187:8001/all_no_active_data"
channels = "http://144.76.187.187:8001/channels"


request_data = requests.get(data) 
request_old_data = requests.get(old_data) 
request_data_channels = requests.get(channels) 
requests_list = [request_data,request_old_data,request_data_channels] 

data_String = str(date.today())+"_"+ "data.json"
data_old_String = str(date.today())+"_"+ "old_data.json"
data_channels_String = str(date.today())+"_"+ "channels.json"
doc_lista = [data_String,data_old_String,data_channels_String] 
i=0

if(request_data or request_old_data or request_data_channels):
    
  
    for e in doc_lista:
        with open(e,'wb') as f: 
            if(f.write(requests_list[i].content)):
                print("Everything goes well"+ str(date.today()))
            else:
                print("Error")
                
        i+=1
else:
    print("Error")





  
    
    
  
    
    
