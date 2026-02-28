import matplotlib.pyplot as plt
import seaborn as sns 

df = sns.load_dataset("tips")

sns.set_style("whitegrid")
sns.set_palette("pastel")

fig,ax=plt.subplots(2,2,figsize=(14,10))

# 1.scatter
sns.scatterplot(ax=ax[0,0],x="total_bill",y="tip",data=df)
ax[0,0].set_title("Total Bill vs Tip")

# 2. Histogram
sns.histplot(ax=ax[0,1],x="tip",data=df,bins=20,kde=True)
ax[0,1].set_title("Tip Distribution")

# 3. Barplot
sns.barplot(ax=ax[1,0],x="sex",y="tip",data=df)
ax[1,0].set_title("Total Bill by Day")

# 4.Boxplot
sns.boxplot(ax=ax[1,1],x="day",y="total_bill",data=df)
ax[1,1].set_title("Total Bill by Day")

plt.tight_layout()
plt.show()