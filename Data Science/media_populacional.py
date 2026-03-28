#Prática 1 — média populacional
import numpy as np
populacao = np.array([2000, 2200, 2500, 2700, 3000, 3200, 3500, 4000, 4200, 5000])
media_populacional = np.mean(populacao)
print("População:", populacao)
print("Média populacional:", media_populacional)


#Prática 2 — média amostral
'''amostra = np.random.choice(populacao, size=4, replace=False)
media_amostral = np.mean(amostra)
print("Amostra:", amostra)
print("Média amostral:", media_amostral)'''


#Prática 3 — várias amostras
'''for i in range(5):
amostra = np.random.choice(populacao, size=4, replace=False)
media_amostral = np.mean(amostra)
print(f"Amostra {i+1}: {amostra} -> média = {media_amostral}")'''


#Prática 4 — tamanho da amostra
'''for tamanho in [2, 4, 6, 8]:
amostra = np.random.choice(populacao, size=tamanho, replace=False)
media_amostral = np.mean(amostra)
print(f"Tamanho da amostra: {tamanho} | média amostral = {media_amostral}")'''


#Simulação

'''import numpy as np
import matplotlib.pyplot as plt
populacao = np.array([2000, 2200, 2500, 2700, 3000, 3200, 3500, 4000, 4200, 5000])
media_populacional = np.mean(populacao)
medias_amostrais = []
for _ in range(100):
    amostra = np.random.choice(populacao, size=4, replace=False)
    medias_amostrais.append(np.mean(amostra))
print("Média populacional:", media_populacional)
print("Média das médias amostrais:", np.mean(medias_amostrais))
plt.hist(medias_amostrais, bins=10, edgecolor='black')
plt.axvline(media_populacional, linestyle='dashed', linewidth=2, label='Média populacional')
plt.xlabel('Médias amostrais')
plt.ylabel('Frequência')
plt.title('Distribuição das médias amostrais')
plt.legend()
plt.show()'''

