import seaborn as sns
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")


def style(df):
    sns.set_style("whitegrid") # other options: darkgrid,whitegrid,dark,ticks

    sns.barplot(x="day",y="total_bill",data=df)
    plt.title("Total Bill by Day")
    plt.show()
style(df)

def palette(df):
    sns.set_palette("deep") # other options: deep,muted,pastel,bright,dark
    sns.barplot(x="sex",y="tip",data=df)
    plt.title("Average Tip by Gender")
    plt.show()
palette(df)

def fig_size_label_color(df):
    plt.figure(figsize=(10,5))
    sns.barplot(x="day",y="total_bill",data=df)
    plt.title("Total Bill by Day",fontsize=16,color="navy")
    plt.xlabel("Day of week",fontsize=12)
    plt.ylabel("Total Bill ($)",fontsize=12)
    plt.show()
fig_size_label_color(df)






