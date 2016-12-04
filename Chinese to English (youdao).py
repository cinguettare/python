#!/usr/bin/python3

import json              # Load json
import urllib.parse      # Load urllib.parse module
import urllib.request    # Load urllib.request module


Chinese = input("Please enter what you need to translate: ")

url = 'http://fanyi.youdao.com/...'                            # Youdao translation page copy url

data = {'type': 'AUTO', 'i': Chinese, 'doctype': 'json', 'xmlVersion': '1.8', 
        'keyfrom': 'fanyi.web', 'ue': 'UTF-8', 'action': 'FY_BY_CLICKBUTTON', 'typoResult': 'true'}
        # analog data

data = urllib.parse.urlencode(data).encode('utf-8')            # Analysis, Change the encoding format

response = urllib.request.urlopen(url, data)                   
html = response.read().decode('utf-8')                         # Conversion encoding

target = json.loads(html)                                      # Use json to convert str to dict

print("English：%s" %target['translateResult'][0][0]['tgt'])   
