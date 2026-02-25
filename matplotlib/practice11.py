import matplotlib.pyplot as plt 

# data 
x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [5,15,20,25]

# First subplot 
plt.subplot(1,2,1) 
plt.plot(x,y1)
plt.title("Line Plot")

# second plot 
plt.subplot(1,2,2)
plt.bar(x,y2)
plt.title("Bar Chart")

plt.show()