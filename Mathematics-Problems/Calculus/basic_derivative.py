# Derivatives of basic

def f(x):
    return x**2
def derivative(x,h=0.0001):
    return (f(x+h)-f(x))/h
test_nums = [1,2,3,4,4,5,6]
for i in range(len(test_nums)): 
    print(f"Derivative of {test_nums[i]} :-> {derivative(test_nums[i])}")
print("The Derivative Basic Problem Solution Completed !")
