
import pandas as pd

def downloading (url):
    df=pd.read_csv(url,encoding='cp1252')
    return df