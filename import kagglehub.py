import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

print("Path to dataset files:", path)

csv_file = os.path.join(path, "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(csv_file)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
print(df.isna().sum())
print(df.nunique())