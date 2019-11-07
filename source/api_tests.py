 # -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:48:20 2019

@author: opujo
"""

import xml.etree.ElementTree as ET
import urllib.request

KEY = "osso:0D5A29001CE009892440"  # my own key
base_url = 'https://api.pinboard.in/v1/'
command = ['posts/all', 'posts/add', 'posts/delete', 'posts/get', 'posts/recent',
           'tags/get', 'tags/delete', 'tags/rename']
filters = ['tag=hot', 'format=xml']


url = "{}{}?auth_token={}".format (base_url, command[0], KEY)

for filt in filters:
    url = url+"&"+filt

with urllib.request.urlopen (url) as fichero:
    temp = fichero.read().decode('utf-8')
    pinboard = ET.fromstring(temp)

#root_pinboard = pinboard.getroot()

for child in pinboard:
    print ("{}: {}\n".format (child.attrib['description'], child.attrib['href']))

    

###################################
# now with json
###################################

import json

filters[1]='format=json'

url = "{}{}?auth_token={}".format (base_url, command[0], KEY)
for filt in filters:
    url = url+"&"+filt
    
with urllib.request.urlopen (url) as fichero:
    temp = fichero.read().decode('utf-8')
    pinboard = json.loads(temp)

# print(json.dumps(pinboard, sort_keys=True, indent=4))

for element in pinboard:
    print ("{}: {}\n".format (element['description'], element['href']))


