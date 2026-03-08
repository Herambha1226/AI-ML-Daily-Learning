# Apply SVD to a real image 

import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

# Load Image 
img = Image.open("art.jpg").convert("L")

# conver image into numpy array 
image_matrix = np.array(img)
print("image matrix : ",image_matrix)
print("Image Matrix Shape : ",image_matrix.shape)

# Apply SVD 
U, S, VT = np.linalg.svd(image_matrix)

print("U shape : ",U.shape)
print("S shape : ",S.shape)
print("VT shape : ",VT.shape)

# plot 
plt.figure()
plt.plot(S)
plt.title("Singular Value Of Image")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.show()

# image recustuction
def recunstruction_image(U,S,VT,K):
    return U[:,:K] @ np.diag(S[:K]) @ VT[:K,:]

# compared Originals vs Compressed
k_values = [5,20,50,100]

plt.figure(figsize=(10,8))

for i, k in enumerate(k_values):
    img_k = recunstruction_image(U,S,VT,k)
    plt.subplot(2,2,i+1)
    plt.imshow(img_k,cmap="gray")
    plt.title(f"K = {k}")
    plt.axis("off")

plt.show()

def explained_variance(S,K):
    return np.sum(S[:k])/np.sum(S**2)

for k in [5,20,50,100]:
    print(f"k={k} explained variance={explained_variance(S,k):.4f}")