import pandas as pd

#Criando um Conjunto de Dados (Dicionário)
dados = {"produtos": ["caneta", "lapis", "borracha"],
         "preço": [2.5, 1.5, 1.0],
         "quantidade": [10, 15, 5]}

#Transformando um Conjunto de Dados em um DataFrame com Pandas
df = pd.DataFrame(dados)
print(df)

#Para salvar um DataFrame como CSV
df.to_csv(".\Aula03\Produtos.csv", index=False)

#Abrindo um Arquivo CSV com Pandas
df = pd.read_csv(".\Aula03\Carros.csv")
print(df)

#Métodos para Exploração de Dados:
df.info() #Exibe informações gerais sobre o DataFrame
df.head() #Exibe as primeiras linhas do DataFrame
df.tail() #Exibe as últimas linhas do DataFrame
df.describe() #Exibe estatísticas descritivas dos dados numéricos
df.describe(include="int64") #Exibe estatísticas descritivas apenas para colunas do tipo float