import pandas as pd
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula05", "arquivos05", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
#df.info()

#5.2 Outliers

# Calcular média e desvio padrão
media = df["vlr_financiamento"].mean()
desvio_padrao = df["vlr_financiamento"].std()
print("media:", media, "desvio_padrao",desvio_padrao)

# Identificar Outliers (valores fora de 3 desvios padrão)
outliers = df[(df["vlr_financiamento"] > media + 3 * desvio_padrao) |
              (df["vlr_financiamento"] < media - 3 * desvio_padrao)]
print(outliers)