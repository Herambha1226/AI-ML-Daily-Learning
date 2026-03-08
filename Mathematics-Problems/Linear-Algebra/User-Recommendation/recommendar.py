import numpy as np
from data import user_item_matrix,users,items


print("User-Item Matrix shape : ",user_item_matrix.shape)

# found user similarity
user_similarity = user_item_matrix @ user_item_matrix.T
print("User Similarity : \n",user_similarity)

# found most similar user
def most_similar_user(user_index):
    similarities = user_similarity[user_index]
    similarities[user_index] = -1
    return np.argmax(similarities)

def recommendation(user_index):
    similar_user = most_similar_user(user_index)

    user_rating = user_item_matrix[user_index]
    similar_user_rating = user_item_matrix[similar_user]

    recommend = []
    for i in range(len(items)):
        if user_rating[i] == 0 and similar_user_rating[i] > 0:
            recommend.append(items[i])
        
    return recommend

# Test 
print("Recommend item for Heramba : ",recommendation(0))
print("Recommend item for Karthikeya : ",recommendation(1))
print("Recommend item for Guptha : ",recommendation(2))
print("Recommend item for Eswara Rao : ",recommendation(3))
print("Recommend item for Gayathri : ",recommendation(4))