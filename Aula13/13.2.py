import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula13", "arquivos13", "financiamentos_2024.csv")

# Leitura do CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# Seleção de atributos e criação da variável alvo
X = df[['vlr_financiamento', 'vlr_subsidio']]
y = df['qtd_uh_financiadas'].apply(lambda x: 1 if x > 5 else 0)  # 1: mais de 5, 0: até 5

# Normalização
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Treinamento
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
modelo = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500, activation='relu', random_state=42)
modelo.fit(X_train, y_train)

# Interação com o usuário
print("=== Previsor de unidades financiadas ===")
while True:
    try:
        financiamento = float(input("Digite o valor do financiamento (em R$): "))
        subsidio = float(input("Digite o valor do subsídio (em R$): "))

        entrada = scaler.transform([[financiamento, subsidio]])
        previsao = modelo.predict(entrada)

        if previsao[0] == 1:
            print(">> Previsão: MAIS DE 5 unidades habitacionais financiadas.")
        else:
            print(">> Previsão: ATÉ 5 unidades habitacionais financiadas.")
        
        continuar = input("Deseja fazer outra previsão? (s/n): ").strip().lower()
        if continuar != 's':
            break
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.\n")