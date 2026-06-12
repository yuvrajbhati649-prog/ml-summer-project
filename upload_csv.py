# upload_csv.py
import pandas as pd

df = pd.read_csv("Social_Network_Ads.csv")
print(df.columns)
print(df.head())
