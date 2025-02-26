import pandas as pd
import os

#5.1 Correlação

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula05", "arquivos05", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
#df.info()

# Converter colunas para o tipo numérico
df["qtd_uh_financiadas"] = df["qtd_uh_financiadas"].astype(int)
df["vlr_financiamento"] = df["vlr_financiamento"].astype(float)

# Calcular correlação
correlacao = df[["qtd_uh_financiadas", "vlr_financiamento"]].corr()
print("Correlação: ",correlacao)