import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(".\Aula04\dados_vendas.csv")

plt.figure(figsize=(10,5))
plt.plot(df["Mes"], df["Vendas"], marker='o', linestyle='-', color='b')
plt.title("Vendas Mensais a partir do CSV")
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")
plt.grid()
plt.show()