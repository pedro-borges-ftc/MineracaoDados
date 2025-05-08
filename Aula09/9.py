# Atividade prática - Aula 09
# Aplicando train_test_split, KFold e SMOTE sobre o dataset "financiamentos_2024.csv"

import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from imblearn.over_sampling import SMOTE

# Montando o caminho completo para o arquivo CSV
caminho = os.path.join("Aula09", "arquivos09", "financiamentos_2024.csv")

# 1. Leitura do CSV com delimitador ";"
df = pd.read_csv(caminho, delimiter=";")
df.info()

# 2. Seleção de colunas relevantes
# Vamos prever a variável "qtd_uh_financiadas" com base nos valores financeiros
X = df[['vlr_financiamento', 'vlr_subsidio']]
y = df['qtd_uh_financiadas']

# 3. Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Formatos dos conjuntos:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

# 4. Validação Cruzada com KFold
print("\nValidação cruzada com KFold:")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for fold, (train_idx, val_idx) in enumerate(kf.split(X_train)):
    print(f"Fold {fold + 1} - Treino: {len(train_idx)} | Validação: {len(val_idx)}")

# 5. Aplicando SMOTE para balanceamento de classes (caso a variável alvo seja categórica)
# Neste exemplo, convertemos y_train em uma variável binária apenas para fins didáticos

# Atenção: SMOTE é adequado apenas para targets categóricos
# Vamos simular uma classificação binária:
# 0 = até 5 unidades financiadas, 1 = mais de 5

import numpy as np
y_train_bin = np.where(y_train > 5, 1, 0)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train_bin)

print("\nApós SMOTE:")
print("X_resampled:", X_resampled.shape)
print("Distribuição das classes após SMOTE:")
print(pd.Series(y_resampled).value_counts())