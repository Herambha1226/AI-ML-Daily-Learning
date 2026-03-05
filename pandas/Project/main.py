#  ------------------------ Student Performance Data Analysis & Cleaning (Real-World Style)---#

import pandas as pd 
import matplotlib.pyplot as plt 

# importing data from students.csv
data = pd.read_csv("pandas/Project/students.csv")

print("\t\tData Types : \n",data.dtypes)
print("\t\tData Information : \n")
data.info()
print("\t\tData Description : \n",data.describe())

# Handling Missing values 
missing_values = data.isnull().sum()
print("\t\tMissing Values Handling : \n",missing_values)
# fill age missing values using mean
data["Age"]=data["Age"].fillna(data["Age"].mean())
#fill Marks With Median 
data["Marks"] = data["Marks"].fillna(data["Marks"].median())
#Fill missing Attendence with mean 
data["Attendance"] = data["Attendance"].fillna(data["Attendance"].mean())


# Converts DataType of a Column float -> int
data["Age"] = data["Age"].astype(int)
data["Marks"] = data["Marks"].astype(int)
data["Attendance"] = data["Attendance"].astype(int)

# Data Filtering  
# 1. Students with Marks > 80 
# 2. Students from IT department
# 3. Students with Attendence < 75 
stu_mark_above_80 = data[data["Marks"] > 80]
stu_from_IT_dept = data[data["Department"]=="IT"]
stu_attend_less_75 = data[data["Attendance"] < 75]

print("Students with Marks > 80 : \n",stu_mark_above_80)
print("Students from IT department : \n",stu_from_IT_dept)
print("Students with Attendence < 75 : \n",stu_attend_less_75)

# Feature Engineering 
def performance(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    else:
        return "Average"
data["Performance"] = data["Marks"].apply(performance) 
print(data)

# ------ GroupBy Analysis -----#
# Average marks per department 
dep_avg = data.groupby("Department")["Marks"].mean()
# Average Attendence Per City
attend_avg = data.groupby("City")["Attendance"].mean()

print("Average marks per department : \n",dep_avg)
print("Average Attendence Per City : \n",attend_avg)


# Visualization 
# Marks Distribution
data["Marks"].plot(kind="hist")
plt.title("Marks Distribution")
plt.show()

# Department vs Average Marks 
data.groupby("Department")["Marks"].mean().plot(kind="bar")
plt.title("Average Marks by Department")
plt.show()

print("Final Cleaned Data : \n",data)


