import matplotlib.pyplot as plt 
import seaborn as sns

DARK_BG = "#0D1117"
ACCENT = "#58A6FF"
GRID_COL = "#21262D"
PALETTE = ["#58A6FF","#3Fb950","#D2A8FF","#FF7872"]

plt.rcParams.update({
    "figure.facecolor": DARK_BG,
    "axes.facecolor" : DARK_BG,
    "axes.edgecolor": GRID_COL,
    "axes.labelcolor" : "#8B949E",
    "xtick.color" : "#8D949E",
    "ytick.color":  "#8D949E",
    "grid.color":GRID_COL,
    "text.color": "#E6EDF3",
    "font.family" : "monospace",
})
sns.set_palette(PALETTE)

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = [412,390,530,610,720,850,
          940,870,760,680,590,980]

fig,ax = plt.subplots(figsize=(10,4))

ax.plot(months,sales,marker="o",lw=2,color=ACCENT)
ax.set_title("Monthly Sales 2024",fontsize=14,pad=12)
ax.set_ylabel("Units Sold")
ax.grid(axis="y",alpha=0.3)

sns.despine(left=True,bottom=True)

plt.tight_layout()
plt.show()