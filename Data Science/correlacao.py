import pandas as pd
import matplotlib.pyplot as plt

latencia_ms = pd.Series([110,115,118,120,121,125,130,135,140,145,300,420])
plt.hist(latencia_ms, bins="auto", color="white",edgecolor="red")
plt.title("Histograma: latência de API (ms)")
plt.xlabel("ms")
plt.ylabel("frequência")
plt.show()





ios = [110,115,118,120,121,125,130,135,140,145]
android = [200,220,240,260,300,420]
plt.hist(ios, bins="auto", alpha=0.7, label="iOS")
plt.hist(android, bins="auto", alpha=0.7, label="Android")
plt.title("Latência por plataforma")
plt.xlabel("ms")
plt.ylabel("Frequência")
plt.legend()
plt.show()




novos = [5,6,7,6,8,5,7,6,5,6,7,8,6,7,5] # maioria curta
recorrentes = [20,22,25,23,21,24,22,23,21,25] # maioria longa
plt.hist(novos, bins="auto", alpha=0.7, label="Novos")
plt.hist(recorrentes, bins="auto", alpha=0.7, label="Recorrentes")
plt.title("Tempo de sessão - Novos vs Recorrentes")
plt.xlabel("Minutos")
plt.ylabel("Frequência")
plt.legend()
plt.show()




# Dois gráficos

import numpy as np

hub_A = [28,29,30,30,31,29,30,31,32,30]
hub_B = [20,22,25,28,30,35,40,55,70,90]
fig, axes = plt.subplots(1, 2, figsize=(10, 4)) #(1,2) representam respectivamente, linha e coluna
axes[0].hist(hub_A, bins="auto", edgecolor='black')
axes[0].set_title("Hub A")
axes[0].set_xlabel("Tempo")
axes[0].set_ylabel("Frequência")
axes[1].hist(hub_B, bins="auto", edgecolor='black')
axes[1].set_title("Hub B")
axes[1].set_xlabel("Tempo")
axes[1].set_ylabel("Frequência")
plt.tight_layout() #repassa o gráfico para que não tenha erros
plt.show()
print("Hub A - média:", np.mean(hub_A))
print("Hub A - mediana:", np.median(hub_A))
print("Hub B - média:", np.mean(hub_B))
print("Hub B - mediana:", np.median(hub_B))



#Correlação Positiva

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,8,9,11,12,14,15] # aumenta junto com x
plt.scatter(x, y, color='blue')
plt.title("Exemplo de correlação positiva")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


#Correlação Negativa

x = [1,2,3,4,5,6,7,8,9,10]
y = [20,18,16,15,14,12,10,9,7,5] # diminui conforme x aumenta
plt.scatter(x, y, color='red')
plt.title("Exemplo de correlação negativa")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


#Sem Correlação

import random

x = list(range(1,11))
y = [random.randint(1,10) for _ in range(10)] # valores aleatórios
plt.scatter(x, y, color='green')
plt.title("Exemplo sem correlação")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()




#Scatter Plot com Outlier
tempo_site = [5,10,15,20,25,30,35,40,45,50,120]
valor_compra = [50,80,100,120,150,160,180,200,210,220,30]
plt.scatter(tempo_site, valor_compra, color='green')
plt.title("Tempo no site vs Valor da compra")
plt.xlabel("Tempo no site (min)")
plt.ylabel("Valor da compra (R$)")
plt.show()