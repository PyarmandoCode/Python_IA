"""
-SQL SERVER
-MYSQL
-POSTGRESS
-ORACLE
-MONGODB, CASSANDRA
"""
import pandas as pd
#Driver que conecta PYTHON con POSTGRESS
import psycopg2
#ORM para poder transformar la tabla en objetos
from sqlalchemy import create_engine

#Conexion a postgress
engine= create_engine("postgresql+psycopg2://admin:admin@localhost:5432/ULTIMOBKCOLLE")

#Leer Tabla

# query = """
#     select 
#     nombrecompleto,
#     aula_id,
#     grado_id,
#     sexo 
# from 
#     public.core_estudiante
# where sexo='Hombre'    

# """

query = """
select 
     nombrecompleto,
     aula_id,
     grado_id,
     sexo 
from 
   public.core_estudiante
"""
#Con SQL PURO
#df_cliente = pd.read_sql(query,engine)
#Leer los primero cinco registros de la tabla
df_estudiantes= pd.read_sql(query,engine)
df_hombres = df_estudiantes[df_estudiantes["sexo"]=="Hombre"]

df_hombres_grado2 = (df_estudiantes["sexo"]=="Hombre") & (df_estudiantes["grado_id"]==2)

#and = &
#or = |

df_hombres_grado2 = df_estudiantes[
    (df_estudiantes["sexo"] == "Hombre") & (df_estudiantes["grado_id"] == 2)
]


print(df_hombres_grado2.head())