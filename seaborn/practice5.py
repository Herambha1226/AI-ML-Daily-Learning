import seaborn as sns
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")

fig, ax = plt.subplots(1,2)

sns.boxplot(ax=ax[0],x="sex",y="tip",data=df)
ax[0].set_title("Tip Distribution by Gender (Boxplot)")

sns.violinplot(ax=ax[1],x="day",y="total_bill",hue="sex",data=df,split=True)
ax[1].set_title("Tip Distribution by Gender (Violin Plot)")

plt.tight_layout()
plt.show()