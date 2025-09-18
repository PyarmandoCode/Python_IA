import pandas as pd

datos  = {
    "Alumno":["Ana","Luis","Sofia","Carlos","Maria"],
    "Edad":[15,16,17,16,18],
    "Nota":[14,18,15,12,20],
    
}

df = pd.DataFrame(datos) #csv,bd,json,api
print(f"DataFrame original:\n {df}")

#Filtra alumnos con nota ,mayor o igual a 15
aprobados= df[df["Nota"]>=15]
print(f"Alumnos Aprobado:\n {aprobados}")

#usando filter
solo_nombre_notas= df.filter(items=["Alumno","Nota"])
print(f"Nombres y Notas:\n {solo_nombre_notas}")

#usar QUERY()
aprobado_query=df.query("Nota>=15")
print(f"Aprobados con query:\n {aprobado_query}")

rango_edades=df.query("Edad>=16 and Edad<=18")
print(f"Rango de edades:\n {rango_edades}")