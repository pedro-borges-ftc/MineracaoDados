from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula06", "arquivos06", "financiamentos_2024_lixo.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Valores vazios no DataSet
df.isnull()

# Soma de Valores vazios no DataSet
df.isnull().sum()

# Usando apenas colunas numéricas
colunas_numericas = df.select_dtypes(include=['int64', 'float64'])

# Removendo dados faltantes do alvo coluna e remove definitivamente
# df.dropna(subset=["num_ano_financiamento"],inplace=True)
# df.dropna(subset=["cod_ibge"],inplace=True)
# df.dropna(subset=["txt_municipio"],inplace=True)
# df.dropna(subset=["txt_uf"],inplace=True)
# df.dropna(subset=["vlr_subsidio"],inplace=True)
df.dropna(subset=["vlr_financiamento"],inplace=True)
df.info()
df.isnull()
df["vlr_financiamento"].isnull().sum()

# Fazer uma lista com os dados faltantes
dados_faltantes = df.columns[df.isnull().any()].tolist()
dados_faltantes

# Não vamos tratar os dados do tipo texto, apenas os Int e Float
dados_faltantes = ['cod_ibge',
 'num_ano_financiamento',
 'vlr_subsidio']

# Criar um método para impeza de dados usando a média
imputer = SimpleImputer(strategy='mean')

# scikit-learn é projetada para treinamento, por isso o fit.
df[dados_faltantes] = imputer.fit_transform(df[dados_faltantes])

#
df.info()

# Soma de Valores vazios no DataSet
df.isnull().sum()