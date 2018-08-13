#! /usr/bin/env python3
import requests
import json

# interface JEEDOM
URL_JEEDOM = "http://192.168.1.46";
API_KEY    = "RJZXkcMWxLPgIOdMDYr9F2pJPNORQgqv";
# connection
URL=URL_JEEDOM+'/core/api/jeeApi.php'
DATA={'apikey' : API_KEY , 'type' : 'scenario' , 'id' : '4', 'action' : 'start'}

print("Test commande ")
response = requests.post(URL, params=DATA)
print("texte: ",response.text)
print("json: ",response.json())
print("url: ",response.url)