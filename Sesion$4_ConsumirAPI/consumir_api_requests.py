import pandas as pd
import requests

url="https://api.escuelajs.co/api/v1/categories"

response= requests.get(url)
data = response.json()

df=pd.DataFrame(data)
print(df.head())