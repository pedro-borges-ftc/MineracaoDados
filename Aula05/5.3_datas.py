import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#5.3 Datas no Pandas

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula05", "arquivos05", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()
df.head(10)

# Converte a coluna 'data_referencia' para datetime
df['data_referencia'] = pd.to_datetime(df['data_referencia'],dayfirst=True)

# Criando novas colunas para o dia, mes e ano
df['dia'] = df['data_referencia'].dt.day
df['mes'] = df['data_referencia'].dt.month
df['ano'] = df['data_referencia'].dt.year

# Exibindo as primeiras linhas do DataFrame com as novas colunas
df.info()
df.head(10)

# Selecionando apenas os dados do ano de 2024 e exibe as primeiras linhas
df_2024 = df[df['num_ano_financiamento'] == 2024]
df_2024.info()
df_2024.head(10)

# Gráfico de barras com seaborn para 
plt.figure(figsize=(10,6))
#No X o UF no Y a quantidade de financiamentos para o ano de 2024
sns.barplot(x="txt_uf", y="qtd_uh_financiadas", data=df_2024, palette="Blues")
plt.title("Quantidade de financiamentos para o ano de 2024")
plt.xlabel("UF")
plt.ylabel("Quantidade de financiamentos")
plt.grid()
#plt.xticks(rotation=90)     #rotaciona para ficar bonitinho
plt.show()

# Selecionando apenas os dados da BAHIA e exibe as primeiras linhas
df_bahia = df[df['txt_uf'] == 'BA']
df_bahia.info()
df_bahia.head(10)

# Gráfico de barras com seaborn para 
plt.figure(figsize=(10,6))
#No X o ANO no Y a quantidade de financiamentos para o estado da BA
sns.barplot(x="num_ano_financiamento", y="qtd_uh_financiadas", data=df_bahia, palette="Blues")
plt.title("Quantidade de financiamentos para o estado da BA")
plt.xlabel("Ano")
plt.ylabel("Quantidade de financiamentos")
plt.grid()
#plt.xticks(rotation=90)     #rotaciona para ficar bonitinho
plt.show()

# Selecionando apenas os dados da Itabuna e exibe as primeiras linhas
df_itabuna = df[(df['txt_uf'] == 'BA') & (df['txt_municipio'] == 'Itabuna ')]
df_itabuna.info()
df_itabuna.head(10)

# Gráfico de barras com seaborn para 
plt.figure(figsize=(10,6))
#No X o ANO no Y a quantidade de financiamentos para o estado da BA
sns.barplot(x="num_ano_financiamento", y="qtd_uh_financiadas", data=df_itabuna, palette="Blues")
plt.title("Quantidade de financiamentos para o município de Itabuna")
plt.xlabel("Ano")
plt.ylabel("Quantidade de financiamentos")
plt.grid()
#plt.xticks(rotation=90)     #rotaciona para ficar bonitinho
plt.show()