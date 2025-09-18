"""
Explicar que ML siempre trabajamos con datos en forma de tabla
introduccion a pandas.DataFrame
"""
import pandas as pd

datos  = {
    "Alumo":["Ana","Luis","Sofia","Carlos","Maria"],
    "Edad":[15,16,17,16,18],
    "Nota_Matematicas":[14,18,15,12,20],
    "Nota_Lengua":[16,17,14,15,19],
}

df = pd.DataFrame(datos) #csv,bd,json,api
print(df)
print(f"Promedio de Matematicas",df["Nota_Matematicas"].mean())
print(f"Promedio de Lengua",df["Nota_Lengua"].mean())