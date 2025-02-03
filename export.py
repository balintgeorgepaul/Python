import requests
import pandas as pd

# Configurare fișier Excel
EXCEL_FILE = "api_data.xlsx"

# Conectare la API
API_URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(API_URL)
data = response.json()

# Transformare în DataFrame
df = pd.DataFrame(data)

# Data Cleansing
df = df.dropna()  # Eliminare valori lipsă
df["title"] = df["title"].str.title()  # Transformare titluri în format titlu

# Salvează datele într-un fișier Excel
df.to_excel(EXCEL_FILE, index=False)

print(f"Datele au fost salvate cu succes in fisierul {EXCEL_FILE}!")
