import requests
import glob
import os
import time
import json

url = "https://eventreminder-6487.restdb.io/rest/eventtable"

headers = {
    'content-type': "application/json",
    'x-apikey': "c22041d43b69ba2e022e2c7a2f2918f995ff7",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", 'https://eventreminder-6487.restdb.io/rest/eventtable/*?q={"match_all": {}}', headers=headers)

print(response.text)

response = requests.request("POST", url, data=open('file.json','rb'), headers=headers)
print(response.text)

list = glob.glob('file.json_*.json')
for jfile in (list):
    os.remove(jfile)

size = (os.path.getsize('file.json') / 1000000)

if (size > 1):
    with open("file.json",'r') as infile:
        o = json.load(infile)
        chunkSize = 200
        for i in range(0, len(o), chunkSize):
            with open("file.json" + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
                json.dump(o[i:i+chunkSize], outfile)
    list = glob.glob('file.json_*.json')
    print(list)
    for jfile in (list):
        print(jfile)
        response = requests.request("POST", url, data=open(jfile,'rb'), headers=headers)
        print(response.text)
else:
    response = requests.request("POST", url, data=open('file.json','rb'), headers=headers)
    print(response.text)

response = requests.request("DELETE", 'https://eventreminder-6487.restdb.io/rest/eventtable/*?q={"Name": "Name"}', headers=headers)
print(response.text)
