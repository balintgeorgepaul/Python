import requests
import pandas as pd

# configure excel file
EXCEL_FILE = "api_data.xlsx"

# appi connection
API_URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(API_URL)
data = response.json()

# create the dataframe
df = pd.DataFrame(data)

# small data cleansing
df = df.dropna()  # Eliminare valori lipsă
df["title"] = df["title"].str.title()  # Transformare titluri în format titlu

# save the data into excel file
df.to_excel(EXCEL_FILE, index=False)

print(f"Data has been saved! {EXCEL_FILE}!")
