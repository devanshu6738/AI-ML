# head and tail method in pandas
import pandas as pd
df=pd.read_csv("Output.csv", encoding='latin1')
print(df.tail(1))
print(df.head(1))
print(df.head())
print(df.tail())