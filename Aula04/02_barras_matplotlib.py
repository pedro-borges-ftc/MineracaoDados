import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
vendas = [2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700]

#Define o tamanho da figura.
plt.figure(figsize=(10,5))

#Cria um gráfico de barras com as vendas mensais.
plt.bar(meses, vendas, color='green')

#Adiciona um título ao gráfico.
plt.title("Vendas Mensais em 2023")

#Adiciona os labels dos eixos x e y.
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")

#Ativa a grade do gráfico.
plt.grid(axis='y')

#Exibe o gráfico.
plt.show()