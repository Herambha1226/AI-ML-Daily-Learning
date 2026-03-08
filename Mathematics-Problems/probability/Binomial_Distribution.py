"""   
A coin is tossed 4 times.

Find probability of getting exactly 2 heads.
"""
import math 

n = 4
k = 2
p = 0.5

prob = math.comb(n,k)*(p**k)*(p**k)
print(prob)
