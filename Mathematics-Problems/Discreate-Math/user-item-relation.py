
user_item = {
    ("U1","Phone"),
    ("U1","Laptop"),
    ("U2","Laptop"),
    ("U3","Phone")
}

print(user_item)

# Domain & Range(important!)
# Math
# Domain = all first elements
# range_ = all second elements

domain = {u for u,i in user_item}
range_ = {i for u,i in user_item}
print("Users : ",domain)
print("Items : ",range_)
