import requests
import simplejson as json


r = requests.get('http://api.zippopotam.us/us/ma/belmont')
j = r.json()

print (j['state'])

for each in j['places']:
    print (each['latitude'])

