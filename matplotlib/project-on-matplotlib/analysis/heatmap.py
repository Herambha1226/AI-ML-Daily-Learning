import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("matplotlib/project-on-matplotlib/data/students.csv")
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("matplotlib/project-on-matplotlib/output/heatmap-result.png")
plt.show()