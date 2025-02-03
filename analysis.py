import pandas as pd
import matplotlib.pyplot as plt

# read excel file generate previously using the file export.py
EXCEL_FILE = "api_data.xlsx"
df = pd.read_excel(EXCEL_FILE)


# 1. Base information about the datasate
print("\n1. Base information:")
print(f"Total number of rows: {len(df)}")
print(f"Total number of columns: {len(df.columns)}")
print("Columns' names:")
print(df.columns.tolist())


# 2. Check distinct values and duplicates
print("\n2. Check distinct values and duplicates:")
print("\nDistinct User ID:", df['userId'].nunique())
print("Total distinct IDs:", df['id'].nunique())

# 3. Grupare dupa userid
print("\n3. Grouping by userId:")
user_counts = df.groupby('userId').size()
print("\nNumber of records per user:")
print(user_counts)

# 5. Verificam daca exista valori lipsa (NULL)
print("\n5. Verificare valori lipsa:")
print(df.isnull().sum())



# 6. Analysis of the lenght of titles and bodies
df['title_length'] = df['title'].str.len()
df['body_length'] = df['body'].str.len()

#grouped = df.groupby(['userId', 'id'])[['title_length', 'body_length']].agg(['sum'])
#print(grouped)


# 7. Top 5 cele mai lungi titluri
print("\n7. Top 5 longest titles:")
print(df.nlargest(5, 'title_length')[['title', 'title_length']])



