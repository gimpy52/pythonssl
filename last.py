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
soup = BeautifulSoup(response.text, 'html.parser')
status = soup.find(class_='main_body')
tatus = soup.find(class_='main_body')
mons = tatus.find_all('td')
for mon in mons:
  st = mon.contents[0]
  print(st)
