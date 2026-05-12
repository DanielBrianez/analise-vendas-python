# ============================================================
# PROJETO: ANÁLISE DE VENDAS COM PYTHON E PANDAS
# OBJETIVO:
# - Ler uma base de vendas em Excel
# - Realizar exploração inicial dos dados
# - Tratar inconsistências na coluna Unit_Price
# - Gerar ranking de vendas por vendedor e categoria
# - Exportar o resultado para um novo arquivo Excel
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LEITURA DA BASE DE DADOS
# ============================================================

ARQUIVO_ORIGEM = "sales_data.xlsx"

df = pd.read_excel(ARQUIVO_ORIGEM)


# ============================================================
# 2. EXPLORAÇÃO INICIAL DOS DADOS (EDA)
# ============================================================

# print("\n=== AMOSTRA DOS DADOS ===")
# print(df.head())

# print("\n=== COLUNAS DA BASE ===")
# print(df.columns)

# print("\n=== INFORMAÇÕES GERAIS ===")
# print(df.info())


# ============================================================
# 3. TRATAMENTO DA COLUNA Unit_Price
# ============================================================

# print("\n=== TIPOS ORIGINAIS EM Unit_Price ===")
# print(df["Unit_Price"].apply(type).value_counts())

df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)

valores_invalidos = df["Unit_Price"].isna().sum()

# print("\n=== VALORES INVÁLIDOS EM Unit_Price ===")
# print(valores_invalidos)

media_unit_price = df["Unit_Price"].mean()

df["Unit_Price"] = df["Unit_Price"].fillna(media_unit_price)

# print("\n=== VALORES NULOS APÓS TRATAMENTO ===")
# print(df["Unit_Price"].isna().sum())


# ============================================================
# 4. ANÁLISES DE VENDAS
# ============================================================

total_por_vendedor = (
    df.groupby("Sales_Rep")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

media_por_categoria = (
    df.groupby("Product_Category")["Sales_Amount"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

vendas_david_food = df[
    (df["Sales_Rep"] == "David") &
    (df["Product_Category"] == "Food")
]

vendas_acima_4000 = df[df["Sales_Amount"] > 4000]

ranking_vendas = (
    df.groupby(["Sales_Rep", "Product_Category"])["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


# ============================================================
# 5. RESULTADOS NO TERMINAL
# ============================================================

# print("\n=== TOTAL DE VENDAS POR VENDEDOR ===")
# print(total_por_vendedor)

# print("\n=== MÉDIA DE VENDAS POR CATEGORIA ===")
# print(media_por_categoria)

# print("\n=== QUANTIDADE DE VENDAS DAVID + FOOD ===")
# print(len(vendas_david_food))

# print("\n=== QUANTIDADE DE VENDAS ACIMA DE 4000 ===")
# print(len(vendas_acima_4000))

# print("\n=== RANKING DE VENDAS POR VENDEDOR E CATEGORIA ===")
# print(ranking_vendas)

# ============================================================
# 6. EXPORTAÇÃO DOS RESULTADOS EM MÚLTIPLAS ABAS
# ============================================================

# ARQUIVO_SAIDA = "relatorio_vendas.xlsx"

# with pd.ExcelWriter(ARQUIVO_SAIDA, engine="openpyxl") as writer:
#     total_por_vendedor.to_excel(
#         writer,
#         sheet_name="Total por Vendedor",
#         index=False
#     )

#     media_por_categoria.to_excel(
#         writer,
#         sheet_name="Media por Categoria",
#         index=False
#     )

#     ranking_vendas.to_excel(
#         writer,
#         sheet_name="Ranking Vendas",
#         index=False
#     )

# print(f"\nRelatório exportado com sucesso: {ARQUIVO_SAIDA}")

# ============================================================
# 7. VISUALIZAÇÃO DOS DADOS
# ============================================================

plt.figure(figsize=(10, 6))

barras = plt.bar(
    total_por_vendedor["Sales_Rep"],
    total_por_vendedor["Sales_Amount"]
)

plt.title(
    "Total de Vendas por Vendedor",
    fontsize=16
)

plt.xlabel(
    "Vendedor",
    fontsize=12
)

plt.ylabel(
    "Valor de Vendas",
    fontsize=12
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura,
        f'R$ {altura:,.0f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()

plt.savefig("grafico_vendas.png")
plt.show()