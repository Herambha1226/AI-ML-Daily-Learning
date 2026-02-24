# 🧪 Practice 1: Line Graph of Marks (Student Performance)

import matplotlib.pyplot as plt

# sujects ,marks
subjects = ["Math","Science","English","Computer"]
marks = [85,90,78,95]

# create line plot 
plt.plot(subjects,marks)

# title & labels
plt.title("Student Marks Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display Graph
plt.show()
