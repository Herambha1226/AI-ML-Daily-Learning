import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")

corr = df.corr(numeric_only=True)

plt.figure(figsize=(7,5))
sns.heatmap(corr,annot=True,cmap="coolwarm",linewidths=0.5,linecolor="black")
plt.title("Correlation Matix Heatmap")
plt.show()