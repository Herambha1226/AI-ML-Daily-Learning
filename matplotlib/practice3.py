# 📈 Practice 3: Stock Price Style Graph

import matplotlib.pyplot as plt

# days and stock price 
days = [1,2,3,4,5,6,7]
price = [100,10,102,108,110,115,120]

plt.plot(days,price,marker="o",linestyle="--",color="green")
plt.title("Stock Price ")
plt.xlabel("Days")
plt.ylabel("Price")

plt.show()