import pandas as pd

data={
    "Name":["Alice","Bob","Charlie","David","Eva"],
    "Age":[24,27,22,32,29],
    "Salary":[50000,54000,58000,60000,62000 ],
    "Performance Score":[88,92,95,85,90],
}

df=pd.DataFrame(data)

#df.loc[row_index,"col_name"]=new value
df.loc[0,"Salary"]=80000

print(df)