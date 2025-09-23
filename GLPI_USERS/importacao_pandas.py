import pandas as pd

diretorio = "C:\\Users\\re049244\\Documents\\Projetos VSCode\\MineracaoDados\\GLPI_USERS\\"

# Carregar planilhas
ad_df = pd.read_excel(diretorio+"AD_Não_Importado.xlsx", usecols=["Name", "UserPrincipalName", "Mail"])
scp_df = pd.read_excel(diretorio+"SCP_Não_Importado.xlsx", usecols=["Nome", "Email"])

print(ad_df.head())
print(scp_df.head())

# Normalizar textos (evitar erros de maiúsculas/minúsculas e espaços)
ad_df["Mail"] = ad_df["Mail"].astype(str).str.strip().str.lower()
ad_df["UserPrincipalName"] = ad_df["UserPrincipalName"].astype(str).str.strip().str.lower()
scp_df["Email"] = scp_df["Email"].astype(str).str.strip().str.lower()
ad_df["Name"] = ad_df["Name"].astype(str).str.strip().str.lower()
scp_df["Nome"] = scp_df["Nome"].astype(str).str.strip().str.lower()

# Cruzar por Email (Mail ↔ Email)
merge_mail = pd.merge(ad_df, scp_df, left_on="Mail", right_on="Email", how="inner")

# Cruzar por UserPrincipalName ↔ Email
merge_upn = pd.merge(ad_df, scp_df, left_on="UserPrincipalName", right_on="Email", how="inner")

# Cruzar por Nome
merge_nome = pd.merge(ad_df, scp_df, left_on="Name", right_on="Nome", how="inner")

# Juntar todos os resultados e remover duplicados
usuarios_importar = pd.concat([merge_mail, merge_upn, merge_nome]).drop_duplicates()

# Exportar resultado para Excel
usuarios_importar.to_excel(diretorio+"Usuarios_Aptos_GLPI.xlsx", index=False)

print("Arquivo gerado: Usuarios_Aptos_GLPI.xlsx")
