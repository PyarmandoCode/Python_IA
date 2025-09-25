import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
edades= np.random.randint(18,60,size=200)
"""
crea un array de 200 edades entre 18 y 59 años ,simulando una poblacion de encuestados
"""

plt.figure(figsize=(8,4))
plt.hist(edades,
         bins=10,
         edgecolor="black",
         color="skyblue",
         alpha=0.9
         )
plt.title("Distribucion de edade")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()