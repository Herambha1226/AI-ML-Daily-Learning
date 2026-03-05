import pandas as pd

data = {
    "Department" : ["IT","HR","IT","Finance","HR"],
    "Salary" : [50000,40000,60000,45000,42000]
}
df = pd.DataFrame(data)

grouped = df.groupby("Department")
print(grouped)
mean_salary = df.groupby("Department")["Salary"].mean()
print("Mean : ",mean_salary)
count_salary = df.groupby("Department")["Salary"].count()
print("Count : ",count_salary)
max_salary = df.groupby("Department")["Salary"].max()
print("Max : ",max_salary)
