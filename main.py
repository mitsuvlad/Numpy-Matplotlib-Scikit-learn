#1
import requests
import json
url = 'https://api.github.com/users/mitsuvlad/repos'
response = requests.get(url)
j_data = response.json()
with open('repo_data.json', 'w') as f:
    json.dump(j_data,f)
for i in j_data:
    print(i['name'])

#2
task 2

