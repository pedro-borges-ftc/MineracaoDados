import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula05", "arquivos05", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

#5.2 Outliers
#Para analisar várias Colunas, vamos usar uma função
def criar_grafico(coluna):
    #criar um gráfico com a coluna
    #plt.figure(figsize=(10, 5))
    sns.boxplot(data=df[coluna])
    #o nome do gráfico terá o mesmo nome da coluna
    plt.title(coluna,fontsize=15)
    #plt.ylim(0, 1000000)

#Criando os gráficos
colunas = [ "qtd_uh_financiadas", "vlr_financiamento", "vlr_subsidio"]

coluna = colunas[0]
#exibindo a média da coluna
print("Media da coluna: ", df[coluna].mean())
#chamando a função para gerar o gráfico para a coluna atual
criar_grafico(coluna)

#vamos verificar quais registros acima da media 
df[coluna].loc[df[coluna] > 114]

#vamos verificar a quantidade de registros acima da media 
df[coluna].loc[df[coluna] > 114].size

#exibindo a média da coluna ignorando outliers
print("Media da coluna ignorando outliers: ", df[coluna].loc[df[coluna] <= 114].mean())