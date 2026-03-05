"""  
These focus on understanding why NumPy exists.

🔥 Problem 1

Create two Python lists of 1 million numbers and add them using:

Normal loop

NumPy vectorization

Measure execution time using time module.
Which one is faster?
"""

import numpy as np
import time

size = 1_000_000
list1 = list(range(size))
list2 = list(range(size))

start_time = time.time()
sum_ = []
for i in range(len(list1)):
    sum_.append(list1[i]+list2[i])
loop_time = time.time() - start_time

print(f"Normal Loop Time: {loop_time:.4f} seconds")

arr1 = np.array(list1)
arr2 = np.array(list2)

start_time = time.time()
sum_arr = arr1 + arr2
vec_time = time.time() - start_time
print(f"Numpy Vectorization Time: {vec_time:.4f} seconds")

print(f"Numpy is {loop_time/vec_time:.1f}x faster")

# numpy version
print(np.__version__)

arrr = np.array([1,2,4,5,6])
print(f"array : {arrr} & Datatype : {arrr.dtype}")


# check memory usage b/w normal list and numpy list
list3 = list(range(1000))
arr3 = np.array(list3)
import sys
real_size = sys.getsizeof(list3) + sum(sys.getsizeof(i) for i in list3)
print(f"Normal List bytes : {real_size}")
print(f"Numpy Array used bytes : {arr3.nbytes}")



# Convert this Python list into NumPy array and multiply every element by 5 without loop:
arr4 = np.array([3,6,9,12])
res = arr4 * 5
print("Result : ",res)