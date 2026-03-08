import numpy as np

data = np.array([12,15,18,20,22,25,30,35,100,105])

# mean
mean = (sum(data)/len(data))
print(f"Mean Of Given Data : {mean}")

# median
# step 1 : sort the array (i use bubble sort)
# step 2 : Check odd/even length
n = len(data)
for i in range(1,n):
    for j in range(0,n-i-1):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
if n%2== 0:
    print("even")
    median = (data[int((n//2)-1)] +data[int(n//2)])/2
    print("Medain : ",median)

else:
    print("odd")
    median = data[int(n//2)]
    print("Medain : ",median)

# mode
data1 = [1,2,2,2,3,3,4,5,6,6,6,6,6]
frequency = {} # empty dictionary
for value in data1:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)
mode = max(frequency,key=frequency.get)
print("Mode: ",mode)


# range
max_value = max(data)
min_value = min(data)
print("Range: ",max_value-min_value)

# variance
data = np.array([12,15,18,20,22,25,30,35,100])
mean = sum(data)/len(data)
deviation = [i-mean for i in data]
square =[d**2 for d in deviation]
variance = sum(square)/len(square)
print("Variance: ",variance)


# Standard deviation
import math
std_deviation = math.sqrt(variance)
print("Standard Deviation: ",std_deviation)

# Effect of Outlier
data = np.array([12,15,18,20,22,25,30,35])
mean = sum(data)/len(data)
deviation = [i-mean for i in data]
square =[d**2 for d in deviation]
variance = sum(square)/len(square)
print("Variance reduced by : ",variance)

# Quartiles(Q1,Q2,Q3)
def quartiles(data):
    data = sorted(data)
    n = len(data)

    # Q2 (median)
    if n % 2 == 0:
        q2 = (data[n//2 - 1] + data[n//2])/2
        lower = data[:n//2]
        upper = data[n//2:]
    else:
        q2 = data[n//2]
        lower = data[:n//2]
        upper = data[n//2 + 1:]

    # Q1
    q1 = np.median(lower)
    q3 = np.median(upper)

    return q1,q2,q3

data = [12,15,18,20,22,25,30,35,100]

q1,q2,q3 = quartiles(data)
print("Q1:",q1)
print("Q2:",q2)
print("Q3:",q3)


# percentile Rank
def percentail_rank(data,value):
    data = sorted(data)
    count = 0

    for x in data:
        if x <= value:
            count += 1
    
    percentile = (count / len(data)) * 100
    return percentile

data = [12,15,18,20,22,25,30,35,100]
print(percentail_rank(data, 25))


# skewness
def skew_type(data):
    data = sorted(data)
    n = len(data)

    mean = sum(data) / n

    # median
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]

    if mean > median:
        return "Right skewed"
    elif mean < median:
        return "Left skewed"
    else:
        return "Symmetric"

data = [12,15,18,20,22,25,30,35,100]
print(skew_type(data))


# visual insight
import matplotlib.pyplot as plt

plt.hist(data,bins=5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Data")
plt.show()