import pandas as pd 

df1 = pd.DataFrame({
    "ID":[1,2,3,4],
    "Name":["Ram","Sam","Riya","Anu"],
})

df2 = pd.DataFrame({
    "ID":[2,3,5],
    "Marks":[88,92,75]
})

inner_merg = pd.merge(df1,df2,on="ID",how="inner")
print("Inner Merge : ",inner_merg)

Left_merg = pd.merge(df1,df2,on="ID",how="left")
print("Left Merge : ",Left_merg)

Outer_merg = pd.merge(df1,df2,on="ID",how="outer")
print("Outer Merge : ",Outer_merg)
