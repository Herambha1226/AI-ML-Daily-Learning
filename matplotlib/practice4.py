# 🧪 Practice 1: Comparing Student Marks (Categories) 
import matplotlib.pyplot as plt 

subjects = ["Math","Science","English","Computer"]
marks = [85,90,78,95]

plt.bar(subjects,marks)

plt.title("Comparing Student Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()
