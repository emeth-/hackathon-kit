import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import json
import django
django.setup()

import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

params = {
    "action": "hi"
}

resp = requests.post("https://github.com/emeth-/hackathon-kit/blob/master/api/views.py", headers=headers, json=params)

print resp.text

#print json.dumps(resp.json(), indent=4)

