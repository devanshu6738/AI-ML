import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df=pd.DataFrame(data)
print(df)
df.to_csv("Output.csv", index=False)
# df.to_excel("Output.xlsx", index=False)
# df.to_json("Output.json", orient='records', lines=True)