import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
vendas = [2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700]

#Define o tamanho da figura.
plt.figure(figsize=(10,5))

#Cria um gráfico de linha.
plt.plot(meses, vendas, marker='o', linestyle='-', color='b')

#Define o título do gráfico.
plt.title("Vendas Mensais em 2023")

#Adiciona os labels dos eixos x e y.
plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")

#Ativa a grade no gráfico.
plt.grid()

#Mostra o gráfico.
plt.show()