import asyncio
import numpy as np 
import cv2
import matplotlib.pyplot as plt 
from concurrent.futures import ThreadPoolExecutor

EXECUTOR = ThreadPoolExecutor(max_workers=4)

def make_image():
    img = np.zeros((400,400,3),dtype=np.uint8)
    for i in range(400):
        img[i, :, 0] = int(255 * i / 400)
        img[i, :, 0] = int(255 * (1 - i / 400))
    
    Y,X = np.ogrid[:400, :400]
    dist = np.sqrt((X- 200)**2 + (Y - 200)**2)
    img[:, :, 1] = (np.sin(dist / 15) * 127 + 128).astype(np.uint8)
    cv2.circle(img, (200,200),80,(255,255,255),3)
    cv2.putText(img, "ASYNC CV",(110, 205),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    return img

def apply_filter(img, name):
    if name == "grayscale":
        return cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    elif name == "blur":
        return cv2.GaussianBlur(img, (21, 21), 0)
    elif name == "edges":
        return cv2.cvtColor(cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 200), cv2.COLOR_GRAY2BGR)
    elif name == "sharpen":
        return cv2.filter2D(img, -1, np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))
    elif name == "heatmap":
        return cv2.applyColorMap(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_JET)
    elif name == "cartoon":
        gray  = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 7)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        return cv2.bitwise_and(cv2.bilateralFilter(img, 9, 300, 300),
                               cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))
    elif name == "emboss":
        return np.clip(cv2.filter2D(img, -1, np.array([[-2,-1,0],[-1,1,1],[0,1,2]])) + 128, 0, 255).astype(np.uint8)
    elif name == "equalize":
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
        return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

async def async_filter(img,name):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EXECUTOR,apply_filter,img,name)

async def async_histogram(img):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EXECUTOR, lambda: { 
        ch: cv2.calcHist([img],[i],None,[256],[0,256]).flatten()
        for i, ch in enumerate(["Blue","Green","Red"])
    })

def show_dashboard(original, results, histogram):
    filters   = ["grayscale","blur","edges","sharpen","heatmap","cartoon","emboss","equalize"]
    accents   = ["#f87171","#fb923c","#fbbf24","#a3e635","#38bdf8","#818cf8","#e879f9","#34d399"]
    fig, axes = plt.subplots(3, 5, figsize=(18, 11), facecolor="#0d0d0d")
    fig.suptitle("⚡ Async OpenCV Pipeline", fontsize=18, color="white", fontweight="bold")
 
    def show(ax, img, title, color="white"):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); ax.set_title(title, color=color, fontsize=9); ax.axis("off")
 
    show(axes[0][0], original, "Original")
    ax_h = axes[0][1]
    ax_h.set_facecolor("#1a1a2e")
    for (ch, vals), col in zip(histogram.items(), ["#5b9cf6","#4ade80","#f87171"]):
        ax_h.plot(vals, color=col, linewidth=1.3, label=ch)
    ax_h.legend(facecolor="#222", labelcolor="white", fontsize=8)
    ax_h.set_title("Histogram", color="white", fontsize=9)
    ax_h.tick_params(colors="gray"); [s.set_color("#333") for s in ax_h.spines.values()]
    [axes[0][c].axis("off") for c in range(2, 5)]
 
    for idx, (name, res) in enumerate(zip(filters, results)):
        r, c = divmod(idx, 4); show(axes[r+1][c], res, name.upper(), accents[idx])
 
    plt.tight_layout()
    plt.savefig("async_cv_output.png", dpi=140, bbox_inches="tight", facecolor="#0d0d0d")
    plt.show()

async def main():
    img = make_image()
    filters = ["grayscale","blur","edges","sharpen","heatmap","cartoon","emboss","equalize"]
    results, histogram = await asyncio.gather(
        asyncio.gather(*[async_filter(img, f) for f in filters]),
        async_histogram(img)
    )
    show_dashboard(img,results,histogram)
    print("Done -> async_cv_output.png")

if __name__ == "__main__":
    asyncio.run(main())

