# Atividade Prática - Seleção de Atributos com SelectKBest e mutual_info_classif
import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_classif

# Criando um dataset fictício
df = pd.DataFrame({
    'idade': [22, 35, 45, 27, 50, 41, 29, 38],
    'salario': [2000, 3500, 5000, 2500, 7000, 6200, 3100, 4500],
    'tempo_empresa': [1, 5, 10, 2, 15, 12, 4, 8],
    'formacao': [2, 3, 4, 2, 5, 4, 3, 4],  # 2: Médio, 3: Técnico, 4: Superior, 5: Pós
    'comprou': [0, 1, 1, 0, 1, 1, 0, 1]  # variável alvo
})

df.info()
df.head(5)

# Separando os dados em variáveis independentes (X) e dependente (y)
X = df[['idade', 'salario', 'tempo_empresa', 'formacao']]
y = df['comprou']

# Aplicando a técnica de seleção de atributos
seletor = SelectKBest(score_func=mutual_info_classif, k=3)
X_novo = seletor.fit_transform(X, y)

# Exibindo os nomes das colunas selecionadas
colunas_selecionadas = X.columns[seletor.get_support()]
print("Colunas selecionadas pelo modelo:", colunas_selecionadas)

# Exibindo o DataFrame reduzido
df_selecionado = pd.DataFrame(X_novo, columns=colunas_selecionadas)
print("\nDataFrame com as colunas selecionadas:")
print(df_selecionado)