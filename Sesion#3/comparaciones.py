import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Asignatura":["Matematica","Historia","Ciencias","Ingles","Arte"],
    "Promedio":[15,12,14,16,18]
}

df= pd.DataFrame(data)
plt.figure(figsize=(8,5))
sns.barplot(x="Asignatura",y="Promedio",data=df,palette="viridis")
plt.title("Promedio de Calificaciones por asignatura")
plt.xlabel("Asignatura")
plt.ylabel("Promedio")
plt.xticks(rotation=10)
plt.show()