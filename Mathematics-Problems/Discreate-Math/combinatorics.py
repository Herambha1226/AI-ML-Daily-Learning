import itertools

# ----- 1. Features (Set theory + combinatorics) ------
features = ["age","income","credit"]

print("Features: ",features)

# 2. All features subset (2^n) ---
print("\nAll features subsets: ")
subsets = []
for r in range(len(features)):
    subsets.extend(itertools.combinations(features,r))
for s in subsets:
    print(s)

print("Total Subset: ",len(subsets))

# ----- 3. Features Combinations (nCr, order doesn't matter)-----
print("\nFeatures combinations (pairs): ")
comb = list(itertools.combinations(features,2))
print(comb)

# ----- 4. Features permutations (nPr, order matters)----
print("\nFeatures permutation (pairs): ")
prem = list(itertools.permutations(features,2))
print(prem)


# --- 5. Hyperparameter grid search (certesian product) ------
learning_rates = [0.01,0.1]
batch_sizes = [16,32]

grid = list(itertools.product(learning_rates,batch_sizes))

print("\nHyperparameter combinations: ")
for g in grid:
    print("lr: ",g[0],"batch: ",g[1])
print("Total models to train: ",len(grid))

