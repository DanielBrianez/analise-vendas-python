# ============================================================
# PROJETO: CONSUMO E ANÁLISE DE API COM PYTHON
# ============================================================

import requests
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. CONSUMO DA API
# ============================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
dados = response.json()


# ============================================================
# 2. CRIAÇÃO DO DATAFRAME
# ============================================================

df = pd.DataFrame(dados)


# ============================================================
# 3. EXPLORAÇÃO INICIAL DOS DADOS
# ============================================================

# print(df.head())
# print(df.columns)
# print(df.info())


# ============================================================
# 4. TRATAMENTO DE JSON ANINHADO - COMPANY
# ============================================================

df["company_name"] = df["company"].apply(
    lambda x: x["name"]
)

df["company_phrase"] = df["company"].apply(
    lambda x: x["catchPhrase"]
)

df["company_bs"] = df["company"].apply(
    lambda x: x["bs"]
)


# ============================================================
# 5. TRATAMENTO DE JSON ANINHADO - ADDRESS
# ============================================================

df["street"] = df["address"].apply(
    lambda x: x["street"]
)

df["room"] = df["address"].apply(
    lambda x: x["suite"]
)

df["city"] = df["address"].apply(
    lambda x: x["city"]
)

df["zipcode"] = df["address"].apply(
    lambda x: x["zipcode"]
)


# ============================================================
# 6. VALIDAÇÃO DOS DADOS TRATADOS
# ============================================================

# print(
#     df[
#         [
#             "name",
#             "company_name",
#             "company_phrase",
#             "company_bs"
#         ]
#     ].head()
# )

# print(
#     df[
#         [
#             "name",
#             "street",
#             "room",
#             "city",
#             "zipcode"
#         ]
#     ].head()
# )


# ============================================================
# 7. ANÁLISE DOS DADOS
# ============================================================

usuarios_por_cidade = (
    df.groupby("city")["name"]
    .count()
    .sort_values(ascending=False)
    .reset_index()
)

usuarios_por_cidade.columns = [
    "Cidade",
    "Quantidade_Usuarios"
]


# ============================================================
# 8. RESULTADOS
# ============================================================

# print(usuarios_por_cidade)

# ============================================================
# 9. VISUALIZAÇÃO DOS DADOS
# ============================================================

plt.figure(figsize=(12, 6))

plt.bar(
    usuarios_por_cidade["Cidade"],
    usuarios_por_cidade["Quantidade_Usuarios"]
)

plt.title(
    "Quantidade de Usuários por Cidade",
    fontsize=16
)

plt.xlabel(
    "Cidade",
    fontsize=12
)

plt.ylabel(
    "Quantidade de Usuários",
    fontsize=12
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "graficos/usuarios_por_cidade.png",
    dpi=300
)

plt.close()