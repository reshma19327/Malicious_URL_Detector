import pandas as pd

df = pd.read_csv("dataset/malicious_phish.csv")

print("Dataset loaded successfully!")
print(df.head())
print("Shape:", df.shape)