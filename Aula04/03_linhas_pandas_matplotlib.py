#Exemplo: Gráfico com Matplotlib e Pandas
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os

#Dicionário com as vendas por mês
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
vendas = [2500, 2700, 2900, 3100, 3300, 1500, 3700, 3900, 1100, 4300, 4500, 4700]

#Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula04", "arquivos", "dados_vendas.csv")

#Criando um DataFrame a partir das listas
df = DataFrame(zip(meses, vendas))
df.columns = ['Mes', 'Vendas']
print(df)

#Para salvar um DataFrame como CSV
df.to_csv(caminho,index=False)

#Abrindo um Arquivo CSV com Pandas
df = pd.read_csv(caminho)
print(df)

#Gráfico com Matplotlib
plt.figure(figsize=(10,5))
plt.plot(df["Mes"], df["Vendas"], marker='o', linestyle='-', color='b')
plt.title("Vendas Mensais a partir do CSV")
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.grid()
plt.show()