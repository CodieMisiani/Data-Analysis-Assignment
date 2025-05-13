import pandas as pd # type: ignore

try:
    df = pd.read_csv('data/yourfile.csv')
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the filename.")
print(df.info())
print(df.isnull().sum())
df = df.dropna()  # OR df.fillna(method='ffill')


print(df.describe())
print(df.groupby('species').mean())

# - Species 2 has the highest average petal length.
# - Sepal width is similar across species.

