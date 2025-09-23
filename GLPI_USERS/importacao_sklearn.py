import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === Carregar planilhas ===
ad_df = pd.read_excel(
    r"C:\Users\re049244\Documents\Projetos VSCode\MineracaoDados\GLPI_USERS\AD_Não_Importado.xlsx",
    usecols=["Name", "UserPrincipalName", "Mail"]
)

scp_df = pd.read_excel(
    r"C:\Users\re049244\Documents\Projetos VSCode\MineracaoDados\GLPI_USERS\SCP_Não_Importado.xlsx",
    usecols=["Nome", "Email"]
)

# Normalização básica
ad_df = ad_df.fillna("").astype(str)
scp_df = scp_df.fillna("").astype(str)

# === Função para encontrar correspondências aproximadas ===
def encontrar_matches(col_ad, col_scp, threshold=0.85):
    """
    Compara duas colunas de texto (AD vs SCP) usando TF-IDF + Cosine Similarity.
    Retorna pares que têm similaridade >= threshold.
    """
    vectorizer = TfidfVectorizer().fit(col_ad.tolist() + col_scp.tolist())
    
    tfidf_ad = vectorizer.transform(col_ad)
    tfidf_scp = vectorizer.transform(col_scp)
    
    sim_matrix = cosine_similarity(tfidf_ad, tfidf_scp)
    
    matches = []
    for i, row in enumerate(sim_matrix):
        j = row.argmax()
        if row[j] >= threshold:
            matches.append((i, j, row[j]))
    
    return matches

# === Comparar por Email ===
matches_email = encontrar_matches(ad_df["Mail"], scp_df["Email"], threshold=0.95)

# === Comparar por Nome ===
matches_nome = encontrar_matches(ad_df["Name"], scp_df["Nome"], threshold=0.90)

# === Juntar os resultados ===
linhas = []

for i, j, score in matches_email + matches_nome:
    linha = {
        "AD_Name": ad_df.loc[i, "Name"],
        "AD_UserPrincipalName": ad_df.loc[i, "UserPrincipalName"],
        "AD_Mail": ad_df.loc[i, "Mail"],
        "SCP_Nome": scp_df.loc[j, "Nome"],
        "SCP_Email": scp_df.loc[j, "Email"],
        "Similaridade": round(score, 3)
    }
    linhas.append(linha)

resultado = pd.DataFrame(linhas).drop_duplicates()

# === Exportar para Excel ===
output_file = r"C:\Users\re049244\Documents\Projetos VSCode\MineracaoDados\GLPI_USERS\Usuarios_Aptos_GLPI.xlsx"
resultado.to_excel(output_file, index=False)

print(f"Arquivo gerado com {len(resultado)} correspondências: {output_file}")