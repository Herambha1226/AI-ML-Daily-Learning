# A u B

data1 = [1,2,3,2,4,5,6,1]
data2 = [7,3,8,9,10,11,2]
train_data = set(data1)
new_data = set(data2)

Union = train_data | new_data
print("A u B : ",Union)
