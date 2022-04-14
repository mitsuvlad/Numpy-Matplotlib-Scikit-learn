#1
import requests
import json
import pandas as pd
url = 'https://api.github.com/users/mitsuvlad/repos'
response = requests.get(url)
j_data = response.json()
with open('repo_data.json', 'w') as f:
     json.dump(j_data,f)
for i in j_data:
     print(i['name'])

#2
from pandas.io.json import json_normalize

version = 5.131
user_id = 168282808
token = "b451fd1fbac3c43551ad98f455bcc92b8da5e2641513b608bb03b12c5fed150288083240981bf4dd6a759"
url = 'https://api.vk.com/method/groups.get'
extended = 1
count = 1000
response = requests.get(url, params={'access_token': token,
                                     'v': version,
                                     'user_id': user_id,
                                     'extended': extended,
                                     'count': count
                                     })
j_data = response.json()

df = json_normalize(j_data['response']['items'])
print(df['name'])





