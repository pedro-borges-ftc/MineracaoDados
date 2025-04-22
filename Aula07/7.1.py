import pandas as pd
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula07", "arquivos07", "financiamentos_2024_lixo.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Convertendo valores para NaN
df['cod_ibge'] = pd.to_numeric(df['cod_ibge'], errors='coerce')
df['vlr_financiamento'] = pd.to_numeric(df['vlr_financiamento'], errors='coerce')
df.info()
df.head(5)

# Calculando a média para substituição
media_cod_ibge = df['cod_ibge'].mean()
media_vlr_financiamento = df['vlr_financiamento'].mean()

# Preenchendo valores NaN com a média
df['cod_ibge'].fillna(media_cod_ibge, inplace=True)
df['vlr_financiamento'].fillna(media_vlr_financiamento, inplace=True)
df.info()
df.head(5)

# Se for a variável alvo (target)
df.dropna(subset=['vlr_financiamento'], inplace=True)
df.info()
df.head(5)