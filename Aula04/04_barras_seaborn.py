#Exemplo: Gráfico com Seaborn, Matplotlib e Pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(".\Aula04\dados_vendas.csv")

plt.figure(figsize=(10,5))
sns.barplot(x="Mes", y="Vendas", data=df, palette="Blues")
plt.title("Vendas Mensais com Seaborn")
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.grid()
plt.show()