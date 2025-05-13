try:
    df = pd.read_csv('data/yourfile.csv')
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the filename.")
