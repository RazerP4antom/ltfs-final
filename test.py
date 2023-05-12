import pandas as pd

df = pd.read_excel('static/files/bajaj.pdf.xlsx')
df.dropna()
print(df)