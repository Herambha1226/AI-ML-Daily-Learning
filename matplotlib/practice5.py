# 🔄 2️⃣ plt.barh() (Horizontal Bar Chart)

import matplotlib.pyplot as plt 

subjects = ["Math","Science","English","Computer"]
marks = [85,90,78,95]

# Horizontal bar graph
plt.barh(subjects,marks)

plt.title("Compare Student By Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()