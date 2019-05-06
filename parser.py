import requests
import pandas as pd
#from pandas.io.json import json_normalize


size = 25
page = 1
r = requests.get(f'https://www.keyforgegame.com/api/decks/?page={page}&page_size={size}')
j = r.json()
df = pd.DataFrame(j['data'])
for page in range(1,1000):
    r = requests.get(f'https://www.keyforgegame.com/api/decks/?page={page}&page_size={size}')
    j = r.json()
    dfTmp = pd.DataFrame(j['data'])
    df = df.append(dfTmp)


