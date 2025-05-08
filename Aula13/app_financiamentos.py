# app_streamlit_financiamentos.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
import tkinter as tk
from tkinter import messagebox

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula13", "arquivos13", "financiamentos_2024.csv")

# Leitura do CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")

# Seleção de atributos e criação do alvo
X = df[['vlr_financiamento', 'vlr_subsidio']]
y = df['qtd_uh_financiadas'].apply(lambda x: 1 if x > 5 else 0)

# Normalização
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Divisão e treinamento
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
modelo = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500, activation='relu', random_state=42)
modelo.fit(X_train, y_train)

# === Função de previsão ===
def prever_unidades():
    try:
        financiamento = float(entry_financiamento.get())
        subsidio = float(entry_subsidio.get())
        
        entrada = scaler.transform([[financiamento, subsidio]])
        previsao = modelo.predict(entrada)
        
        if previsao[0] == 1:
            resultado = "MAIS DE 5 unidades financiadas"
        else:
            resultado = "ATÉ 5 unidades financiadas"
        
        messagebox.showinfo("Resultado da Previsão", f"Previsão: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Erro inesperado", str(e))

# === Interface gráfica com Tkinter ===
janela = tk.Tk()
janela.title("Previsor de Unidades Financiadas")
janela.geometry("400x250")
janela.resizable(False, False)

tk.Label(janela, text="Valor do Financiamento (R$):").pack(pady=5)
entry_financiamento = tk.Entry(janela)
entry_financiamento.pack(pady=5)

tk.Label(janela, text="Valor do Subsídio (R$):").pack(pady=5)
entry_subsidio = tk.Entry(janela)
entry_subsidio.pack(pady=5)

tk.Button(janela, text="Prever", command=prever_unidades, bg="#4CAF50", fg="white").pack(pady=15)
tk.Button(janela, text="Sair", command=janela.destroy).pack()

janela.mainloop()