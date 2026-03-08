import numpy as np
def f(v):
    x,y = v 
    return np.array([x**2+y,x+y**2])
def jacobian(v,h=1e-5):
    n = len(v)
    m = len(f(v))
    j = np.zeros((m,n))

    for i in range(n):
        v_h = v.copy()
        v_h[i] += h
        j[:, i] = (f(v_h) - f(v))/h
    return j
print(jacobian(np.array([2.0,3.0])))
