import requests
import pandas as pd
#from pandas.io.json import json_normalize

s = 25

def expandDataFrameOnDisk(nPages = 10, filename = 'exampleDataFrame.pkl'):

    df = pd.read_pickle('exampleDataFrame.pkl')

    tail  = readInAPI(nPages, firstPage= len(df)//25+1)
    df = df.append(tail)

    df.to_pickle(filename)
    
    return df


def loadDataFrame(filename = 'exampleDataFrame.pkl'):
    return pd.read_pickle('exampleDataFrame.pkl')



def readInAPI(nPages, firstPage = 1):
    page = 1
    r = requests.get(f'https://www.keyforgegame.com/api/decks/?page={page}&page_size={s}')
    j = r.json()
    df = pd.DataFrame(j['data'])
    for page in range(1,nPages):
        r = requests.get(f'https://www.keyforgegame.com/api/decks/?page={page}&page_size={s}')
        j = r.json()
        dfTmp = pd.DataFrame(j['data'])
        df = df.append(dfTmp, ignore_index=True)

    return df







#def createCardsTable(nPages, firstPage=1):
