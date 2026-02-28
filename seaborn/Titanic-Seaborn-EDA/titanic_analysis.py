# Titanic Data Analysis using Seaborn 

# import packages are pandas,seaborn,matplotlib
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

# data load 
df = sns.load_dataset("titanic")

print("First 5 Rows : \n")
print(df.head())

print("\nDataset Info : \n")
print(df.info())

print("\nMissing Values : \n")
print(df.isnull().sum())

fig, ax = plt.subplots(2,3,figsize=(6,4))

# Surviaval Count Plot 
sns.countplot(ax=ax[0,0],x="survived",data=df)
ax[0,0].set_title("Survival Count (0 = Not Survived,1 = Survived)")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_Count.png",dpi=300,bbox_inches='tight')

# survival based on Gender 
sns.countplot(ax=ax[0,1],x="sex",hue="survived",data=df)
ax[0,1].set_title("Survival Based On Gender")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_based_gender.png",dpi=300,bbox_inches='tight')

#Survival based on passenger class
sns.countplot(ax=ax[0,2],x="class",hue="survived",data=df)
ax[0,2].set_title("Survival Rate based on passenger Class")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_based_class.png",dpi=300,bbox_inches='tight')

# Age Distribution 
sns.histplot(ax=ax[1,0],x="age",data=df,kde=True)
ax[1,0].set_title("Age Distribution Of Passenger")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_age_distribution.png",dpi=300,bbox_inches='tight')

# Boxplot (Age vs Class)
sns.boxplot(ax=ax[1,1],x="class",y="age",data=df)
ax[1,1].set_title("Age Distribution by Passenger Class")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_age_vs_class.png",dpi=300,bbox_inches='tight')

# Correlation Heatmap (Very Important)
corr = df.corr(numeric_only=True)
sns.heatmap(corr,ax=ax[1,2],annot=True,cmap="coolwarm")
ax[1,2].set_title("Correlation Heatmap")
fig.savefig("seaborn/Titanic-Seaborn-EDA/images/Survival_heatmap.png",dpi=300,bbox_inches='tight')

plt.show()