# ============================================================
# PROJETO: CONSUMO DE API COM PYTHON
# ============================================================

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
dados = response.json()
df = pd.DataFrame(dados)

print(df.head())