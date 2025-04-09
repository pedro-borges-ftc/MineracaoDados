# Atividade Prática Integrada - Mineração de Dados com Pandas, Matplotlib e Seaborn
# Tema: Finanças Pessoais

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leitura e preparação dos dados
df = pd.read_csv("financas_pessoais.csv", delimiter=",")

# Convertendo colunas de data
df["cadastro"] = pd.to_datetime(df["cadastro"], dayfirst=True)
df["vencimento"] = pd.to_datetime(df["vencimento"], dayfirst=True)

# Garantindo que 'valor' é float
df["valor"] = df["valor"].astype(float)

# 2. Análise inicial
print("=== Primeiras linhas ===")
print(df.head())

print("\n=== Últimas linhas ===")
print(df.tail())

print("\n=== Informações gerais ===")
df.info()

print("\n=== Estatísticas descritivas ===")
print(df.describe())

# 3. Análise de correlação
print("\n=== Correlação entre colunas numéricas ===")
print(df.corr(numeric_only=True))

# Gráfico de dispersão entre valor e data de vencimento
plt.figure(figsize=(10, 5))
sns.scatterplot(x="vencimento", y="valor", hue="tipoLancamento", data=df)
plt.title("Dispersão entre Valor e Data de Vencimento")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Detecção de Outliers
media = df["valor"].mean()
desvio = df["valor"].std()

outliers = df[(df["valor"] > media + 3 * desvio) | (df["valor"] < media - 3 * desvio)]

print("\n=== Outliers Identificados ===")
print(outliers)

# Boxplot para visualização dos outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x="tipoLancamento", y="valor", data=df)
plt.title("Boxplot dos Valores por Tipo de Lançamento")
plt.grid(True)
plt.show()

# 5. Visualizações adicionais
# Gráfico de barras - quitado x não quitado
plt.figure(figsize=(6, 4))
df["quitado"].value_counts().plot(kind="bar", color=["green", "red"])
plt.title("Status de Quitação")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Gráfico de linha - soma de lançamentos por mês
df["mes"] = df["vencimento"].dt.to_period("M")

df_mensal = df.groupby("mes")["valor"].sum().reset_index()
df_mensal["mes"] = df_mensal["mes"].astype(str)

plt.figure(figsize=(10, 5))
sns.lineplot(x="mes", y="valor", data=df_mensal, marker="o")
plt.title("Total de Lançamentos por Mês")
plt.xticks(rotation=45)
plt.ylabel("Valor Total (R$)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras agrupadas - receitas vs despesas por cliente
grouped = df.groupby(["nome_cliente", "tipoLancamento"])["valor"].sum().unstack().fillna(0)

grouped.plot(kind="bar", figsize=(12, 6))
plt.title("Receitas e Despesas por Cliente")
plt.ylabel("Valor Total (R$)")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.tight_layout()
plt.show()