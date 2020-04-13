import logging
import requests
import os
import json
from requests.exceptions import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://192.168.100.1/cgi-bin/cm_state_cgi"

response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parse')
#jsonResponse = json.dumps(response.json())
#print(response.content)
print(response.text)
jsonC = json.dumps(response.content)
print(jsonC)
#with urlopen(url) as r:
#     result = json.loads(r.read().decode(r.headers.get_content_charset('utf-8')))
#print(result)
