# ============================================================
# PROJETO: ANÁLISE DE VENDAS COM SQL, PYTHON E PANDAS
# ============================================================

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONEXÃO COM O BANCO DE DADOS SQLITE
# ============================================================

conexao = sqlite3.connect("sales.db")


# ============================================================
# LEITURA DA BASE DE DADOS
# ============================================================

df = pd.read_excel("sales_data.xlsx")


# ============================================================
# IMPORTAÇÃO DOS DADOS PARA O SQLITE
# ============================================================

df.to_sql(
    "sales_data",
    conexao,
    if_exists="replace",
    index=False
)


# ============================================================
# CONSULTA SQL
# ============================================================

query = """
SELECT
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Vendas
FROM sales_data
GROUP BY Sales_Rep
ORDER BY Total_Vendas DESC
"""


# ============================================================
# EXECUÇÃO DA QUERY SQL
# ============================================================

resultado = pd.read_sql_query(query, conexao)

print(resultado)


# ============================================================
# VISUALIZAÇÃO DOS DADOS
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    resultado["Sales_Rep"],
    resultado["Total_Vendas"]
)

plt.title("Total de Vendas por Vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Total de Vendas")

plt.tight_layout()

plt.savefig(
    "graficos/sql_total_vendas_por_vendedor.png",
    dpi=300
)

plt.show()