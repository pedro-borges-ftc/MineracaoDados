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