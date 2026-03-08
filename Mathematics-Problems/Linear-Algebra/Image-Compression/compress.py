import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

img = Image.open("art.jpg")
img = np.array(img,dtype=float)/255.0

print("Shape Of Image Matrix : ",img.shape)

# --- SVD for one channel ---
def compress_channel(channel, k):
    U, S, Vt = np.linalg.svd(channel, full_matrices=False)
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]

# --- Compress full color image ---
def compress_image(img, k):
    compressed = np.zeros_like(img)

    for c in range(3):  # R, G, B
        compressed[:, :, c] = compress_channel(img[:, :, c], k)

    return np.clip(compressed, 0, 1)


ks = [5,25,50,100]
os.makedirs("output",exist_ok=True)

for i,k in enumerate(ks):
    compressed_image = compress_image(img,k)

    plt.subplot(2,2,i+1)
    plt.imshow(compressed_image)
    plt.title(f"k : {k}")
    plt.axis("off")

    Image.fromarray((compressed_image*255).astype(np.uint8)) \
               .save(f"output/compressed_k_{k}.jpg")
    
plt.tight_layout()
plt.show()
