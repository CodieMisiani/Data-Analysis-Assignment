import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.datasets import load_iris # type: ignore

try:
    df = pd.read_csv('data/yourfile.csv')
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the filename.")
