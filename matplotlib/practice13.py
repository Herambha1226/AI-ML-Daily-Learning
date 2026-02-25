import matplotlib.pyplot as plt 

#data 
x = [1,2,3,4,5]
marks = [50,60,70,80,90]

fig, ax = plt.subplots(1,2)

# First 
ax[0].plot(x,marks)
ax[0].set_title("Marks Trend")
ax[0].set_xlabel("Test Number")
ax[0].set_ylabel("Marks")

# Second 
ax[1].hist(marks)
ax[1].set_title("Marks Distribution")

plt.show()