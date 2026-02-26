import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

data = np.array([
    [1,0.8,0.3],
    [0.8,1,0.6],
    [0.3,0.6,1]
])

sns.heatmap(data,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()