import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")

fig, ax = plt.subplots(1,2,figsize=(12,5))

# Gender vs Tip 
sns.barplot(ax=ax[0],x="sex",y="tip",data=df)
ax[0].set_title("Average Tip by Gender")

# Day vs Toatal Bill
sns.countplot(ax=ax[1],x="sex",data=df)
ax[1].set_title("Count of Customers by gender")

plt.show()