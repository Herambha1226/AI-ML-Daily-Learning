import matplotlib.pyplot as plt 
import seaborn as sns 

df = sns.load_dataset("tips")

print(df)

sns.scatterplot(x="total_bill",y="tip",data=df)
plt.show()