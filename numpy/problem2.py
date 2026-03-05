import numpy as np

# 1D Slicing
# First three elements

# Last three elements

# Every second element

arr = np.array([5,10,15,20,25,30])
print("First three elements : ",arr[0:3])
print("Last Three Numbers : ",arr[-3:])
print("Every second element : ",arr[::2])

# ------- problem 2 ------- #
""" 
Given:

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])


Print:

Element 50

Entire second row

Entire first column
"""
arr1 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])


print("Element 50 : ",arr1[(1,1)])
print("Entire Second Row : ",arr1[:2])
print("First Column : ",arr1[:,0])

""" 
From above matrix extract:

[[50,60],
 [80,90]]

"""
print("Extract Sub MAtrix :\n ",arr1[1:,1:])


"""
Given:

arr = np.array([12, 25, 7, 40, 18])


Return all numbers:
"""
arr2 = np.array([12,25,7,40,18])
print("Greter Than 20 : ",arr2 > 20)
print("Less than 15 : ",arr2 < 15)



""" 
From this matrix:

arr = np.array([[3,8,1],
                [9,2,7],
                [4,6,5]])


Return all values greater than 5.
"""
arr4 = np.array([[3,8,1],
                 [9,2,7],
                 [4,6,5]
                 ])
print("All vaues greater than 5 : ",arr4[arr4 > 5])



# Fancy Indexing 
arr5 = np.array([100,200,300,400,500])
print("100, 300, 500 : ",arr5[[0,2,len(arr5)-1]])
print("100 and 200 and 400 : ",arr5[[0,1,len(arr5)-1]])
