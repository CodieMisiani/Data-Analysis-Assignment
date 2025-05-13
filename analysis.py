import pandas as pd # type: ignore

try:
    df = pd.read_csv('data/yourfile.csv')
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the filename.")
print(df.info())
print(df.isnull().sum())
df = df.dropna()  # OR df.fillna(method='ffill')
