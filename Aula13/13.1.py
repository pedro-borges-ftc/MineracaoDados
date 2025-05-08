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

# Seleção de colunas
X = df[['vlr_financiamento', 'vlr_subsidio']]

# Criando uma variável alvo binária: 0 (até 5 unidades) ou 1 (mais de 5)
y = df['qtd_uh_financiadas'].apply(lambda x: 1 if x > 5 else 0)

# Normalização dos dados
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Treinamento da RNA
modelo = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500, activation='relu', random_state=42)
modelo.fit(X_train, y_train)

# Previsão
y_pred = modelo.predict(X_test)

# Avaliação
acc = accuracy_score(y_test, y_pred)
print("Acurácia do modelo:", round(acc * 100, 2), "%")