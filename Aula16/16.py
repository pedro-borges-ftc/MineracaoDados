import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from tkinter import Tk, Label, Entry, Button, messagebox

# 0. Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula16", "Movimentacoes_Aeroportuarias_202401.csv")

# 1. Leitura do CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# 2. Tratamento de colunas numéricas
colunas_numericas = ['QT_PAX_LOCAL', 'QT_PAX_CONEXAO_DOMESTICO',
                     'QT_PAX_CONEXAO_INTERNACIONAL', 'QT_CORREIO', 'QT_CARGA']
for col in colunas_numericas:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Remover linhas com valores faltantes nessas colunas
df.dropna(subset=colunas_numericas, inplace=True)

# 4. Análise de correlação
plt.figure(figsize=(10,6))
sns.heatmap(df[colunas_numericas].corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlação entre variáveis numéricas")
caminho = os.path.join("Aula16", "grafico_correlacao.png")
plt.savefig(caminho)

# 5. Criar coluna alvo: alta movimentação é quando QT_PAX_LOCAL > 150
df['ALTA_MOVIMENTACAO'] = df['QT_PAX_LOCAL'].apply(lambda x: 1 if x > 150 else 0)

# 6. Seleção de atributos para o modelo
X_raw = df[['QT_PAX_CONEXAO_DOMESTICO', 'QT_PAX_CONEXAO_INTERNACIONAL', 'QT_CORREIO', 'QT_CARGA']]
y = df['ALTA_MOVIMENTACAO']

# 7. Normalização dos dados
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_raw)

# 8. Seleção de atributos
selector = SelectKBest(score_func=mutual_info_classif, k=3)
X_selected = selector.fit_transform(X_scaled, y)
colunas_escolhidas = X_raw.columns[selector.get_support()]
print("Colunas selecionadas:", colunas_escolhidas.tolist())

# 9. Validação com train_test_split e KFold
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.3, random_state=42)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for i, (train_idx, val_idx) in enumerate(kf.split(X_train)):
    print(f"Fold {i+1}: Treino={len(train_idx)}, Validação={len(val_idx)}")

# 10. Treinamento do modelo
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500, random_state=42)
model.fit(X_train, y_train)

# 11. Avaliação do modelo
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acc*100:.2f}%")

# 12. Script interativo com Tkinter
def prever():
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
        v3 = float(entry3.get())
        dados = scaler.transform([[v1, v2, 0, v3]])
        dados = selector.transform(dados)
        resultado = model.predict(dados)
        if resultado[0] == 1:
            msg = "Alta movimentação prevista (>150 passageiros locais)"
        else:
            msg = "Movimentação regular prevista (até 150 passageiros)"
        messagebox.showinfo("Resultado da Previsão", msg)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

app = Tk()
app.title("Previsor de Movimentação de Passageiros")
app.geometry("400x250")

Label(app, text="PAX conexão doméstico:").pack()
entry1 = Entry(app)
entry1.pack()

Label(app, text="PAX conexão internacional:").pack()
entry2 = Entry(app)
entry2.pack()

Label(app, text="Carga (kg):").pack()
entry3 = Entry(app)
entry3.pack()

Button(app, text="Prever", command=prever, bg="green", fg="white").pack(pady=10)
Button(app, text="Sair", command=app.quit).pack()

app.mainloop()