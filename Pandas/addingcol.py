import pandas as pd

data={
    "Name":["Alice","Bob","Charlie","David","Eva"],
    "Age":[24,27,22,32,29],
    "Salary":[50000,54000,58000,60000,62000 ],
    "Performance Score":[88,92,95,85,90],
}

df=pd.DataFrame(data)

#adding new col df["col_name"]="data"

df["Bonus"]=df["Salary"]*0.1
print(df)

#using insert(loc,"col_name",some_data)
df.insert(0,"Employee_ID",[10,20,30,40,50])
print(df)
