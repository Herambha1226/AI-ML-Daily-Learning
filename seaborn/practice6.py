import seaborn as sns
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")

sns.pairplot(df,hue="sex")

sns.jointplot(x="total_bill",y="tip",data=df,kind="reg")
plt.show()
