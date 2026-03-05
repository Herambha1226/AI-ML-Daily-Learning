"""Easy Level
Problem 1:

Create a Series with values:

[5, 15, 25, 35]


Then print the second element."""

import pandas as pd

s = pd.Series([5,15,25,35])
print(s)

""" 
Problem 2:

Create a Series with custom index:
Values = [100, 200, 300]
Index = ["a", "b", "c"]
Access value of index "b"."""

cus_s = pd.Series([100,200,300],index=["a","b","c"])
print("Custom Index : \n",cus_s)
print(cus_s["b"])


"""
Problem 3:

Create a DataFrame:

Name: ["Asha", "Ravi", "Kiran"]
Marks: [85, 90, 78]


Then:

Print only Marks column

Print first row"""

data = {
    "Name" : ["Asha","Ravi","Kiran"],
    "Marks" : [85,90,78]
}
df = pd.DataFrame(data)
print(df)
print(df["Marks"])
print(df.loc[0])

"""
Problem 4 (ML Style Filtering 🔥)

Create a Series:

[10, 45, 60, 20, 80]


Print values greater than 40."""
series = pd.Series([10,45,60,30,80])
print(series[series > 40])

"""
Problem 5:

Create this DataFrame:

Name   Age   Score
Ram    20    88
Sam    21    76
Riya   19    92


Tasks:

Print only “Score” column

Print rows where Score > 80"""

data2 = {
    "Name" : ["Ram","Sam","Riya"],
    "Age" : [20,21,19],
    "Score" : [88,76,92]
}
df2 = pd.DataFrame(data2)
print(df2["Score"])
print(df2[df2["Score"] > 80])

"""
Create a DataFrame:

Name: ["Anu", "Vijay", "Rohit", "Sneha"]
Marks: [45, 82, 67, 90]


Tasks:

Print students with Marks > 70

Print only Names where Marks < 60"""

data3 = {
    "Name" : ["Anu","Vijay","Rohit","Sneha"],
    "Marks" : [45,82,67,90]
}
df4 = pd.DataFrame(data3)
print(df4[df4["Marks"] > 70])
print(df4[df4["Marks"] < 60]["Name"])
print(df4[df4["Name"]=="Rohit"]["Marks"])
print(df4.loc[df4["Name"]=="Rohit", "Marks"])