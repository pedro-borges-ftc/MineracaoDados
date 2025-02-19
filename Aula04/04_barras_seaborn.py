#Exemplo: Gráfico com Seaborn, Matplotlib e Pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula04", "arquivos", "dados_vendas.csv")

df = pd.read_csv(caminho)

plt.figure(figsize=(10,5))
sns.barplot(x="Mes", y="Vendas", data=df, palette="Blues")
plt.title("Vendas Mensais com Seaborn")
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.grid()
plt.show()