import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#5.1 Correlação

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula05", "arquivos05", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Quero ver somente os valores numericos, int e float, posso excluir o resto
val_num = df.select_dtypes(exclude=['object','datetime'])
relacao = val_num.corr()
print(relacao)

# Criando mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(relacao, annot=True, cmap="YlGnBu")
plt.show()

# salvando um mapa de calor em para png
plt.savefig("heatmap.png", format="png")