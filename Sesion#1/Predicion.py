"""
Predecir si un alumno aprobara en base a su promedio
"""
import pandas as pd

datos  = {
    "Alumo":["Ana","Luis","Sofia","Carlos","Maria"],
    "Edad":[15,16,17,16,18],
    "Nota_Matematicas":[14,18,15,12,20],
    "Nota_Lengua":[16,17,14,15,19],
}

df = pd.DataFrame(datos) #csv,bd,json,api
#Agregar column promedio

df["Promedio"] = (df["Nota_Matematicas"] + df["Nota_Lengua"]) / 2

#Clasificar : Aprobado si promedio mayor a 14
df["Estado"] =df["Promedio"].apply(lambda x: "Aprobado" if x>=14 else "Desaprobado")


def cuadrado(x):
    return x * x

cuadrado = lambda x: x * x #filter() sorted() apply() map() 
print(df)