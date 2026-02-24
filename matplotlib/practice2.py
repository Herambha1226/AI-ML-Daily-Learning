# 🌡️ Practice 2: Temperature Graph (Real-World Data)
import matplotlib.pyplot as plt 

# Days and Temperature 
days = [1,2,3,4,5,6,7]
temperature = [32,34,33,35,36,37,38]

# plot 
plt.plot(days,temperature)

# title & Labels 
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temeperature Graph")

# show Graph 
plt.show()