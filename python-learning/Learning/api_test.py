import requests
import json

token = 'Personal Token Here'
username = 'Bazhful'
url = 'https://api.github.com/users/bazhful/repos'


session = requests.Session()
session.auth = (username, token)
repos = json.loads(session.get(url).text)


params = {"state": "open",}
headers = {'Authorization': token}
r = requests.get(url, auth=(username, token)).json()
#requests.post
#requests.delete
#requests.modify

for i in r:
    print(i['name'])
