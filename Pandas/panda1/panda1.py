import pandas as pd

#read data from a CSV file
df=pd.read_csv("data.csv",encoding='latin1')
# df1=pd.read_excel("data.xlsx")
# df2=pd.read_json("D:\AI ML\AI-ML\Pandas\panda1\data.json")
print(df)
#gcsfs is a library to read and write files from Google Cloud Storage
