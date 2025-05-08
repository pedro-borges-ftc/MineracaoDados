import pandas as pd
import os

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula08", "arquivos08", "financiamentos_2024.csv")

# Lendo o arquivo CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Criando uma lista com os valores da coluna txt_uf
lista_UFs = df["txt_uf"].tolist()

# Quantidade total de dados
qtd_total = len(lista_UFs)

# Identificando os estados diferentes
UFs_diferentes = set(lista_UFs)
qtd_diferentes = len(UFs_diferentes)

print(qtd_total)
print(UFs_diferentes)
print(qtd_diferentes)

# Contar quantas vezes um estado específico aparece (ex: "BA")
qtd_vezes = lista_UFs.count("BA")
print(qtd_vezes)

# Filtrando o DataFrame para remover linhas onde txt_uf == 'RR'
df = df[df['txt_uf'] != 'RR']

# Criando uma lista com os valores da coluna txt_uf
lista_UFs = df["txt_uf"].tolist()

# Atualizando a lista e as contagens\lista_UFs = df["txt_uf"].tolist()
qtd_total = len(lista_UFs)
UFs_diferentes = set(lista_UFs)
qtd_diferentes = len(UFs_diferentes)

print(qtd_total)
print(UFs_diferentes)
print(qtd_diferentes)