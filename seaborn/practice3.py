import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")

fig, ax = plt.subplots(1,3,figsize=(12,5))

# Histogram + KDE
sns.histplot(ax=ax[0],x="total_bill",data=df,kde=True)
ax[0].set_title("Total Bill Distribution")

# KDE Plot with comparision
sns.kdeplot(ax=ax[1],x="tip",hue="sex",data=df,fill=True)
ax[1].set_title("Tip Distribution by Gender")

# Displot 
sns.displot(ax=ax[2],x="tip",data=df,kde=True)
ax[2].set_title("Basic Distribution Plot")


plt.show()