from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula07", "arquivos07", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Selecionando colunas para treinamento
colunas_treinamento = df[['cod_ibge', 'num_ano_financiamento','qtd_uh_financiadas','vlr_financiamento','vlr_subsidio']]

# Criando o objeto de escala
escala = MinMaxScaler()
colunas_normalizadas = escala.fit_transform(colunas_treinamento)

# Resultado
print(colunas_normalizadas)