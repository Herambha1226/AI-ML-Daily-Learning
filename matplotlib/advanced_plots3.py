from scipy.signal import argrelextrema
import numpy as np
import matplotlib.pyplot as plt

DARK_BG = "#0D1117"
ACCENT  = "#58A6FF"

plt.rcParams.update({
    "figure.facecolor": DARK_BG,
    "axes.facecolor":   DARK_BG,
    "axes.edgecolor":   "#21262D",
    "text.color":       "#E6EDF3",
    "xtick.color":      "#8B949E",
    "ytick.color":      "#8B949E",
    "grid.color":       "#21262D",
})

x = ["Jan","Feb","Mar","Apr","May","Jun",
     "Jul","Aug","Sep","Oct","Nov","Dec"]
y = [412, 390, 530, 610, 720, 850,
     940, 870, 760, 680, 590, 980]

fig, ax = plt.subplots(figsize=(10, 5))

peak_idx = np.argmax(y)
peak_x   = x[peak_idx]
peak_y   = y[peak_idx]

text_idx = min(peak_idx + 2, len(x) - 1)   
text_x   = x[text_idx]

ax.annotate(
    f"Peak\n{peak_y:.1f}",
    xy      = (peak_x, peak_y),
    xytext  = (text_x, peak_y * 0.82),
    arrowprops=dict(
        arrowstyle       = "->",
        color            = ACCENT,
        connectionstyle  = "arc3,rad=-0.3",   
        lw               = 1.5,
    ),
    fontsize = 10,
    color    = ACCENT,
    bbox     = dict(
        boxstyle = "round,pad=0.4",           
        fc       = DARK_BG,
        ec       = ACCENT,
        lw       = 1,
    ),
)

ax.plot(x, y, marker="o", lw=2, color=ACCENT)
ax.set_title("Monthly Sales 2024", fontsize=14, pad=12)
ax.set_ylabel("Units Sold")
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()