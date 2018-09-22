import requests
import glob
import os
import time
import json
import re

url = "https://eventreminder-6487.restdb.io/rest/eventtable?q={}&max=3&sort=Start Time&dir=1"

headers = {
    'content-type': "application/json",
    'x-apikey': "c22041d43b69ba2e022e2c7a2f2918f995ff7",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
