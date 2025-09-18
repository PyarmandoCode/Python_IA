"""
Repaso de Python
- Variables y tipos basicos (int , float , str , bool)
- Estructuras Basicas:
    - Listas (Colleciones ordenadas)
    - Diccionarios (Pares Clave-Valor)
- Librerias Fudamentales

"""
import numpy as np
import pandas as pd

#Crear una lista de edades de estudiantes
edades= [15,16,17,16,18]
#Calcular promedio usando python
#Usando Funciones
promedio = sum(edades) / len(edades)

acum=0
con=0
#Iterando mediante un bucle
for numero in edades:
    acum +=numero  #acumular los datos de la lista
    con = con + 1 #contar la cantidad de elementos
promedio = acum/con
print(f"El Promedio de edades de personas es: {promedio}")
#Usando la libreria numpy
print(f"El Promedio de edades de personas es: {np.mean(edades)}")