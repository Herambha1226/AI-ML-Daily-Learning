import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("face.jpg"))
lum_img = img[:, :, 0]

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].imshow(img)
ax[0].set_title("Original")

ax[1].imshow(lum_img, cmap="hot")
ax[1].set_title("Heatmap")

ax[2].hist(lum_img.ravel(), bins=256, fc='k', ec='k')
ax[2].set_title("Luminance Histogram")

plt.tight_layout()
plt.show()