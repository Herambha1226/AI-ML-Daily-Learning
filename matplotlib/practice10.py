# Advanced ML Style Scatter Plot 
import matplotlib.pyplot as plt 

study_hours = [1,2,3,4,5,6,7,8]
marks = [30,40,50,60,65,75,85,95]

plt.scatter(study_hours,marks,color="pink",marker="o",s=90,alpha=0.7)

plt.title("Study Hours vs Marks (ML Analysis)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.show()
