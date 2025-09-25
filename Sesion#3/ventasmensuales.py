import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Mes":["Enero","Febrero","Marzo","Abril","Mayo","Junio"],
    "Ventas":[1200,1500,1800,1700,2100,2500]
}

df= pd.DataFrame(data)

#Tamaño de la figura en pulgadas (ancho,alto)
plt.figure(figsize=(8,4))
plt.plot(df["Mes"],df["Ventas"],
         marker="o",
         linestyle="-",
         linewidth=2)
plt.title("Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.grid(True)
plt.tight_layout()
plt.show() #Renderiza /visualiza el grafico
         