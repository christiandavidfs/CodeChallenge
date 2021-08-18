import re, urllib
import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
import jsonreader



query = "dogs"
r = requests.get('https://api.duckduckgo.com/?q=dogecoin&format=json')
data = r.json()


paster=jsonreader.extract_element_from_json(data, ["RelatedTopics","url"])

print(paster)