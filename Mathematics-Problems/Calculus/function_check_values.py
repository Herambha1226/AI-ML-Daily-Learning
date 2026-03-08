def f(x):
    return x**2 - 4*x
def derivative(x,h=0.0001):
    return (f(x+h)-f(x))/h
test_num = [1,2,3,4,5]
for i in range(len(test_num)):
    result = derivative(test_num[i])
    if result < 0:
        print(f"{test_num[i]}:-> negative  {result}")
    elif result > 0:
        print(f"{test_num[i]}:-> positive  {result}")
    else :
        print(f"{test_num[i]}:-> zero  {result}")