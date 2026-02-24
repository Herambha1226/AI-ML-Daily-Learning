# 🤖 Real ML Use Case: Model Accuracy Comparison 

import matplotlib.pyplot as plt 

models = ["Logistic Regrssion","SVM","Random Forest","KNN"]
accuracy = [85,88,92,80]

plt.bar(models,accuracy)
plt.title("Models Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")

plt.show()

# graph with mutiple color bars 
plt.bar(models,accuracy,color=["green","orange","red","pink"])
plt.title("Models Accuracy Comparision")
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")

plt.show()