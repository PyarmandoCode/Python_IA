import matplotlib.pyplot as plt

empresas = ["Sodimax","Bata","Plaza Vea","ISIL"] 
participacion=[35,25,20,20]

plt.figure(figsize=(6,6))
plt.pie(participacion,
        labels=empresas,
        autopct="%1.1f%%",
        startangle=90,
        explode=(0.05,0,0,0))

plt.title("Participacion de mercado")
plt.axis("equal")
plt.show()