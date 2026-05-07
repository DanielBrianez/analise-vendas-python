# ============================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ============================================================

# Importa a biblioteca pandas e define o apelido "pd"
# Pandas é utilizado para manipulação e análise de dados
import pandas as pd


# ============================================================
# LEITURA DA BASE DE DADOS
# ============================================================

# Lê o arquivo Excel "sales_data.xlsx"
# e armazena os dados em um DataFrame chamado "df"
df = pd.read_excel("sales_data.xlsx")


# ============================================================
# EXPLORAÇÃO INICIAL DOS DADOS (EDA)
# ============================================================

# Mostra as 5 primeiras linhas da tabela
# Útil para visualizar uma amostra dos dados
# print(df.head())

# Mostra o nome de todas as colunas da base
# print(df.columns)

# Mostra informações gerais da base:
# - quantidade de linhas
# - quantidade de colunas
# - tipos de dados
# - valores nulos
# print(df.info())


# ============================================================
# INVESTIGAÇÃO DA COLUNA "Unit_Price"
# ============================================================

# Mostra as 5 primeiras linhas da coluna "Unit_Price"
# para validar os valores presentes
# print(df["Unit_Price"].head())

# Verifica os tipos de dados existentes na coluna
# e conta quantos valores existem de cada tipo
# print(df["Unit_Price"].apply(type).value_counts())


# ============================================================
# LIMPEZA E TRATAMENTO DOS DADOS
# ============================================================

# Converte os valores da coluna "Unit_Price" para numérico
#
# errors="coerce":
# caso algum valor não possa ser convertido,
# ele será transformado em NaN (valor nulo)
df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)

# Calcula a média da coluna "Unit_Price"
# ignorando automaticamente os valores nulos (NaN)
media = df["Unit_Price"].mean()

# Substitui os valores nulos (NaN)
# pela média calculada anteriormente
df["Unit_Price"] = df["Unit_Price"].fillna(media)


# ============================================================
# VALIDAÇÃO FINAL
# ============================================================

# Conta quantos valores nulos ainda existem
# na coluna "Unit_Price"
# O resultado esperado é 0
# print(df["Unit_Price"].isna().sum())