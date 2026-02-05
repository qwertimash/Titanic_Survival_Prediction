import pandas as pd

url = "https://raw.githubusercontent.com/adamerose/datasets/refs/heads/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())

survival_rate = df.groupby('Sex')['Survived'].mean() * 100
print(survival_rate)
