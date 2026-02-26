import matplotlib.pyplot as plt 

plt.style.use("fivethirtyeight")  #uses dark_background or ggplot or seaborn or fivethirtyeight

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x, y)
plt.title("Styled Graph - ggplot")
plt.show()