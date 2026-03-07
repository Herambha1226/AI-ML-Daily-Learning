# Dimensionality Reduction : Reduce number of features
# Example : 
# Dataset feature = 100 
# Reduce to = 20 features

# Benefits : 
# Faster Training
# Less Overfitting
# Better Visualization

from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder,StandardScaler
import pandas as pd 

df = pd.read_csv("DATA-CLEANING/datasets/Data-To-Use.csv")

df = df.dropna()

categorical_col = df.select_dtypes(include=["object","string"]).columns

le = LabelEncoder()
for col in categorical_col:
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(df_scaled)
print(X_pca)

