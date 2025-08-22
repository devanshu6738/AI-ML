"""
how big is your dataset
what is the name of cloumns
shape and column
"""
import pandas as pd

data={
    "Name":["Alice","Bob","Charlie","David","Eva"],
    "Age":[24,27,22,32,29],
    "Salary":[50000,54000,58000,60000,62000 ],
    "Performance Score":[88,92,95,85,90],
}

df=pd.DataFrame(data)

print('Shape:',df.shape)
print('column:',df.columns)