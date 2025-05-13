import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Step 1: Load the dataset
try:
    df = pd.read_csv('data/yourfile.csv')
    print(df.head())
except FileNotFoundError:
    print("The file was not found. Please check the filename.")

# Step 2: Handle missing values
print(df.info())
print(df.isnull().sum())
df = df.dropna()  # OR df.fillna(method='ffill')

# Step 3: Compute basic statistics
print(df.describe())
print(df.groupby('species').mean())

# Step 4: Visualize the data
# Line Chart
df['index'] = df.index
plt.plot(df['index'], df['sepal length (cm)'])
plt.title('Sepal Length Over Samples')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Bar Chart
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title('Average Petal Length by Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# Histogram
df['sepal width (cm)'].plot(kind='hist', bins=20)
plt.title('Distribution of Sepal Width')
plt.show()

# Scatter Plot
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# Step 5: Write findings
# Findings:
# - The petal length increases with sepal length.
# - Species 1 shows a wider variation in sepal width.