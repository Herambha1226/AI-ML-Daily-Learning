# here you see how model works inside training

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. Create Dataset
# -----------------------------
np.random.seed(42)

n_samples = 100

# Useful features
area = np.random.rand(n_samples) * 1000
bedrooms = np.random.randint(1, 5, n_samples)

# Useless features
color = np.random.rand(n_samples)  # random noise
owner_id = np.random.rand(n_samples)  # random noise

# Target (only depends on area + bedrooms)
price = 3000 * area + 50000 * bedrooms + np.random.randn(n_samples) * 10000

# Combine features
X = np.column_stack([area, bedrooms, color, owner_id])
y = price

feature_names = ["Area", "Bedrooms", "Color", "OwnerID"]

# -----------------------------
# 2. Scale Data (important!)
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# 3. Train ElasticNet
# -----------------------------
model = ElasticNet(alpha=0.5, l1_ratio=0.7)
model.fit(X_scaled, y)

# -----------------------------
# 4. Print Weights
# -----------------------------
print("Feature Weights:\n")
for name, coef in zip(feature_names, model.coef_):
    print(f"{name}: {coef:.4f}")

# -----------------------------
# 5. Visualization
# -----------------------------
plt.figure()
plt.bar(feature_names, model.coef_)
plt.title("Feature Importance (Weights)")
plt.xlabel("Features")
plt.ylabel("Weight Value")
plt.show()
