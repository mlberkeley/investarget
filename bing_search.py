#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
import httplib
import pprint
import csv
import json
import pandas as pd


def bing_search(query):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    # query string parameters
    payload = {'q': query}
    # custom headers
    headers = {'Ocp-Apim-Subscription-Key': '418c759db6fb4604b1e494c7e0511651'}
    # make GET request
    r = requests.get(url, params=payload, headers=headers)
    # get JSON response
    return r.json()

j = bing_search('Qualtrics')

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(j.get('webPages', {}).get('value', {}))

data = j.get('webPages', {}).get('value', {})

with open('/Users/kunalsingh/Documents/ML@Berkeley/Investarget/bing_json.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=True, encoding="utf-8")


df = pd.read_json('/Users/kunalsingh/Documents/ML@Berkeley/Investarget/bing_json.json')
print(df)       
df.to_csv('/Users/kunalsingh/Documents/ML@Berkeley/Investarget/bing_data.csv')







