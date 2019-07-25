#!/usr/bin/python

import yaml
import json
import urllib
yaml = YAML()
#stream = open("/tmp/example.yaml", 'r')
#data_loaded = yaml.safe_load(stream)
#print(data == data_loaded)

#my_dict = yaml.load(open('/tmp/example.yaml'))
#print my_dictA

#data = {}  
#data['people'] = []  
#data['people'].append({  
#    'name': 'Scott',
#    'website': 'stackabuse.com',
#    'from': 'Nebraska'
#    })
#data['people'].append({  
#    'name': 'Larry',
#    'website': 'google.com',
#    'from': 'Michigan'
#    })
#data['people'].append({  
#    'name': 'Tim',
#    'website': 'apple.com',
#    'from': 'Alabama'
#    })

stream = open("/tmp/example.yaml", 'r')
print(yaml.dump(stream, default_flow_style=False))
#data_loaded = yaml.dump(stream, default_flow_style=False)
#print(data_loaded)
#for doc in data_loaded:
#   for k,v in doc.items():
#       print k, "->", v
#   print "\n",
