import pandas as pd

df_colombia = pd.read_csv('colombia.csv')
df_norway = pd.read_csv('norway.csv')
df_honduras = pd.read_csv('honduras.csv')
df_mtwashington = pd.read_csv('mt-washington.csv')

df = df_colombia._append(df_norway)
df = df._append(df_honduras)
df = df._append(df_mtwashington)

df.to_csv('data.csv', index=False)


