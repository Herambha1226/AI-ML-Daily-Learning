import numpy as np
import matplotlib.pyplot as plt

# Scalar : A Scalar is single value. it means represent only one value.
learning_rate = 0.01
ephocs = 100

print("Learning Rate : ",learning_rate)
print("ephocs : ",ephocs)

# Vector : A vector is a 1D array.

student_scores = np.array([88,92,85])

print("Student Score : ",student_scores)
print("Shape : ",student_scores.shape)

# Vector Operations
weights = np.array([0.3,0.4,0.3])

weighted_score = np.dot(student_scores,weights)
print("Weighted Score : ",weighted_score)

# Matrix : A matrix is combination of rows & columns . it is a 2D. Example we say it is Dataset.
class_score = np.array([
    [90,95,99],
    [85,90,87],
    [91,89,84],
    [96,82,94]
])

print("Class Scores : \n",class_score)
print("shape : ",class_score.shape)

# mean score as per the suject
subject_mean = np.mean(class_score,axis=0)
print("Subject per socre : ",subject_mean)

# mean Score as per the student
student_mean = np.mean(class_score,axis=1)
print("Score per Student : ",student_mean)

# matrix multiplication
weights = np.array([0.2,0.5,0.4,0.1])

prediction = np.dot(student_mean,weights)  # This is exactly how neural networks work internally.
print("Pridiction Score : ",prediction) 

# Tensors : A tensor is a 3D.it combinatios of matrices. Also , the Tensor defines 3 and above Dimensions.
# gray scale images
images = np.random.rand(10,28,28)
print("Images Shapes (gray scale) : ",images.shape)

# colores scale images. it is a 4D image
images_color = np.random.rand(10,28,28,3)  # in the last parameter is 3 because every pixel has red,blue and green pixels in pixel it is useful for the colored images.
print("Image Shape (colored) : ",images_color)

# visualize Tensor
plt.imshow(images[0],cmap="gray")
plt.title("Sample Images")
plt.axis("off")
plt.show()

