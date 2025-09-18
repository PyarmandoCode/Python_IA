import pandas as pd

#Cargar un archivo csv

df = pd.read_csv("datos.csv")

#primeras filas
#print(df.head())
#Resumen estadistico
#print(df.describe())

#Agrupar ventas por producto
ventas_producto = df.groupby("producto")["monto"].sum().reset_index()
#print(ventas_producto)

#Guardar un nuevo csv
ventas_producto.to_csv("ventas_por_producto.csv",index=False)