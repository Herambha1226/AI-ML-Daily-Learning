import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
df = sns.load_dataset("iris")

def annotate_mean(data, **kwargs):
    m = data['sepal_length'].mean()
    ax = plt.gca()
    ax.text(0.8, 0.1, f'μ={m:.2f}', 
            transform=ax.transAxes, 
            fontweight='bold', 
            fontsize=10)

g = sns.FacetGrid(df, row="species", hue="species", aspect=4, height=1.5)

g.map(sns.kdeplot, "sepal_length", fill=True, alpha=1, lw=1.5, bw_adjust=.5)
g.map(sns.kdeplot, "sepal_length", color="white", lw=2, bw_adjust=.5)

g.map(plt.axhline, y=0, lw=2, clip_on=False)

g.map_dataframe(annotate_mean)

def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
    
g.map(label, "sepal_length")

g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

plt.subplots_adjust(hspace=-.25) 
plt.show()