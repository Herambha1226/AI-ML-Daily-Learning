import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
math_marks = [70,75,80,85,90]
science_marks = [65,70,78,82,88]

plt.plot(x,math_marks,label="Math")
plt.plot(x,science_marks,label="Science")

plt.title("Marks Comparison")
plt.xlabel("Exam Number")
plt.ylabel("Marks")
#  plt.xlim(1,3) # Only Show the 1 to 3 on X-axis
plt.legend() # show Labels
plt.show()

days = [1,2,3,4,5]
steps = [3000,5000,7000,4000,8000]
plt.plot(days,steps)
plt.xticks([1,2,3,4,5])