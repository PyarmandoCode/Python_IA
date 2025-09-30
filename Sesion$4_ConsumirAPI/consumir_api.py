import pandas as pd

"""
url de tu API 
"""
url="http://127.0.0.1:8000/api/productos/"

"""
cargar datos JSON a Dataframe
"""

df=pd.read_json(url)
print(df.head())
