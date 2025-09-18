import pandas as pd
import numpy as np

#Crear un Dataframe 

data = {
    "nombre":["Juan","Pedro","Miguel","Maria",None],
    "edad":[20,None,22,25,23],
    "grado":[2,3,None,2,1]
}

df= pd.DataFrame(data)
df["edad"] = df["edad"].fillna(0)
df["grado"]=df["grado"].fillna(df["grado"].mean())



#df_fill= df.fillna("Desconocido")

print(df)

