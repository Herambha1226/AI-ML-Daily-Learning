""" 
ay 2: Basic Plots

Core plots:

sns.scatterplot()

sns.lineplot()

Practice mini project:

Tips dataset analysis

Bill vs Tip visualization"""
import matplotlib.pyplot as plt 
import seaborn as sns 

df = sns.load_dataset("tips")

fig, ax = plt.subplots(1,4)

sns.scatterplot(ax=ax[0],x="total_bill",y="tip",data=df)
ax[0].set_title("Total Bill vs Tip (Scatter Plot)")

sns.histplot(ax=ax[1],x="tip",data=df)
ax[1].set_title("Tip Distribution (Histogram)")

sns.barplot(ax=ax[2],x="sex",y="tip",data=df)
ax[2].set_title("Who are Give More Tips ?")

sns.lineplot(ax=ax[3],x="day",y="tip",data=df)
ax[3].set_title("Average Tip by Day")

plt.show()