import numpy as np
import matplotlib.pyplot as plt
import sys

x0 = -2.0
if len(sys.argv) >= 2:
    x0 = np.float(sys.argv[1])
gamma = 0.1
if len(sys.argv) >= 3:
    gamma = np.float(sys.argv[2])
n_loop = 5
if len(sys.argv) >= 4:
    n_loop = int(sys.argv[3])

def f(x):
    if x<0:
        return x*x
    if x>=0 and x<=1:
        return x
    if x>1:
        return 2*x-1

def df(x):
    if x<0:
        return 2*x
    if x>=0 and x<=1:
        return 1
    if x>1:
        return 2

def g(x):
    return pow(x,4) - 2*pow(x,3)

def dg(x):
    return 4*(x**3) - 6*(x**2)

func = f
deriv = df
gd_x = [x0]
gd_y = [func(x0)]
rng = 4
f_point_x = np.arange(x0 - rng, x0 + rng, 0.01)
f_point_y = [func(x) for x in f_point_x]
x_ = x0

for _ in range(n_loop):
    x_ = x_ - gamma*deriv(x_)
    gd_x.append(x_)
    gd_y.append(func(x_))

plt.plot(f_point_x, f_point_y, 'r')
#plt.axis([x0 - rng, x0 + rng, -5,5])
plt.show()
print(gd_x)
print(gd_y)