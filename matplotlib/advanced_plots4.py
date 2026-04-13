import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import seaborn as sns

DARK_BG  = "#0D1117"
PANEL_BG = "#161B22"
ACCENT   = "#58A6FF"
GREEN    = "#3FB950"
ORANGE   = "#F78166"
MUTED    = "#8B949E"
GRID_COL = "#21262D"

plt.rcParams.update({
    "figure.facecolor":  DARK_BG,
    "axes.facecolor":    PANEL_BG,
    "axes.edgecolor":    GRID_COL,
    "axes.labelcolor":   MUTED,
    "xtick.color":       MUTED,       # ✓ fixed: was xticks.color
    "ytick.color":       MUTED,       # ✓ fixed: was yticks.color
    "grid.color":        GRID_COL,
    "grid.linestyle":    "--",
    "grid.alpha":        0.4,
    "text.color":        "#E6EDF3",
    "font.family":       "monospace",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "legend.framealpha": 0.15,
    "legend.edgecolor":  GRID_COL,
})

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = np.array([412,390,530,610,720,850,
                   940,870,760,680,590,980])
target = np.full(12, 700)
growth = np.diff(sales) / sales[:-1] * 100
x      = np.arange(12)

categories = ["Electronics","Clothing","Food","Books","Sports"]
cat_sales  = [48200,31500,27800,15600,22100]

fig = plt.figure(figsize=(16, 9))
fig.suptitle("Sales Dashboard 2024", fontsize=18,
             fontweight="bold", color="#E6EDF3", y=0.98)

gs = gridspec.GridSpec(
    2, 2,
    figure=fig,
    hspace=0.45,
    wspace=0.35,
    height_ratios=[1.6, 1]
)

ax_main  = fig.add_subplot(gs[0, :])
ax_bar   = fig.add_subplot(gs[1, 0])
ax_growth= fig.add_subplot(gs[1, 1])

# ── MAIN CHART ───────────────────────────────────────────────────────
ax_main.plot(x, sales, color=ACCENT, lw=2.5,
             marker="o", ms=5, zorder=3, label="Sales")

ax_main.fill_between(x, sales, target,
    where=(sales >= target),
    color=GREEN, alpha=0.15, label="Above target")
ax_main.fill_between(x, sales, target,
    where=(sales < target),
    color=ORANGE, alpha=0.15, label="Below target")

ax_main.axhline(y=700, color=ORANGE, lw=1.2,
                linestyle="--", label="Target 700", zorder=2)

# inset zoom
axins = ax_main.inset_axes([0.78, 0.08, 0.2, 0.45])
axins.plot(x[-3:], sales[-3:], color=ACCENT, marker="o", lw=2)
axins.set_facecolor(DARK_BG)
axins.tick_params(labelsize=8, colors=MUTED)
axins.set_xticks([9, 10, 11])
axins.set_xticklabels(["Oct", "Nov", "Dec"])
ax_main.indicate_inset_zoom(axins, edgecolor=MUTED)

# peak annotation
peak_idx = np.argmax(sales)
text_idx = min(peak_idx + 2, 11)
ax_main.annotate(
    f"Peak\n{sales[peak_idx]}",
    xy     =(peak_idx, sales[peak_idx]),
    xytext =(text_idx, sales[peak_idx] * 0.80),
    arrowprops=dict(arrowstyle="->", color=ACCENT,
                    connectionstyle="arc3,rad=-0.3", lw=1.5),
    fontsize=9, color=ACCENT,
    bbox=dict(boxstyle="round,pad=0.4",
              fc=PANEL_BG, ec=ACCENT, lw=1),
)

ax_main.set_xticks(x)
ax_main.set_xticklabels(months)
ax_main.set_ylabel("Units Sold")
ax_main.set_title("Monthly Sales vs Target", pad=10)
ax_main.legend(loc="upper left", fontsize=9)
ax_main.grid(axis="y")

# dual y-axis
ax2 = ax_main.twinx()
ax2.plot(x[1:], growth, color=GREEN, lw=1.2,
         linestyle="--", alpha=0.7, label="Growth %")
ax2.set_ylabel("MoM Growth %", color=GREEN)
ax2.tick_params(axis="y", colors=GREEN)
ax2.axhline(0, color=GREEN, lw=0.5, alpha=0.4)

# ── BAR CHART ────────────────────────────────────────────────────────
colors = [ACCENT if v == max(cat_sales) else MUTED for v in cat_sales]
bars   = ax_bar.barh(categories, cat_sales, color=colors, height=0.6)
ax_bar.bar_label(bars, fmt="₹%.0f", padding=5,
                 fontsize=8, color="#E6EDF3")
ax_bar.set_title("Revenue by Category", pad=10)
ax_bar.set_xlabel("Revenue (₹)")
ax_bar.grid(axis="x")
ax_bar.invert_yaxis()

# ── GROWTH BARS ──────────────────────────────────────────────────────
bar_colors = [GREEN if g >= 0 else ORANGE for g in growth]
ax_growth.bar(x[1:], growth, color=bar_colors, width=0.6)
ax_growth.axhline(0, color=MUTED, lw=0.8)
ax_growth.set_xticks(x[1:])
ax_growth.set_xticklabels(months[1:], rotation=45, ha="right")
ax_growth.set_title("Month-on-Month Growth %", pad=10)
ax_growth.set_ylabel("Growth (%)")
ax_growth.grid(axis="y")

plt.savefig("dashboard.png", dpi=150,
            bbox_inches="tight", facecolor=DARK_BG)
plt.show()