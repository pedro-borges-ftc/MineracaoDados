import pandas as pd
import matplotlib.pyplot as plt
import os

#Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula04", "arquivos", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
#df.columns = ["data_referencia","cod_ibge","txt_municipio","txt_uf","num_ano_financiamento","qtd_uh_financiadas","vlr_financiamento","vlr_subsidio"]

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Convertendo colunas numéricas para os tipos adequados
df["num_ano_financiamento"] = df["num_ano_financiamento"].astype(int)
df["qtd_uh_financiadas"] = df["qtd_uh_financiadas"].astype(int)
df["vlr_financiamento"] = df["vlr_financiamento"].astype(float)
df["vlr_subsidio"] = df["vlr_subsidio"].astype(float)

# Exibir informações do DataFrame
print(df.info())

# Exibir estatísticas descritivas das colunas numéricas
print(df.describe())

# Criando um gráfico de linhas para o valor de financiamento ao longo dos anos
plt.figure(figsize=(10, 5))
#plt.bar(df["num_ano_financiamento"], df["vlr_financiamento"],color='b')
plt.plot(df["num_ano_financiamento"], df["vlr_financiamento"], marker='o', linestyle='-', color='b', label="Valor Financiado")

# Adicionando título e rótulos
plt.title("Evolução do Valor de Financiamento")
plt.xlabel("Ano de Financiamento")
plt.ylabel("Valor do Financiamento (R$)")
plt.grid(True)
plt.legend()

# Exibindo o gráfico
plt.show()