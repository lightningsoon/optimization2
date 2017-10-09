import sympy
import matplotlib.pyplot as plt
import numpy as np

Epsilon = 0.01
t = sympy.symbols('t')

# y=t*(t+2)
y = t ** 3 - 2 * t + 1
f=lambda t:t ** 3 - 2 * t + 1
t0 = 0.5#初始值




y_diff1 = sympy.diff(y, t)
y_diff2 = sympy.diff(y, t, 2)
k = 1
def Next_t(t0):
    global k
    delta = (y_diff1 / y_diff2).subs(t, t0)
    t1 = (t - delta).subs(t, t0)
    # print(t1)
    if abs(delta) < Epsilon:
        print('第%d次迭代：%f=%f%+f' % (k, t1, t0, -delta))
        plt.plot([t1], [f(t1)], marker='o', markersize=8, markerfacecolor="red")
        plt.text(t1, f(t1), k, color='red', fontsize=k*2 + 10)
        return t1
    else:
        print('第%d次迭代：%f=%f%+f' % (k, t1, t0, -delta))
        plt.plot([t1], [f(t1)], marker='o', markersize=8, markerfacecolor="green")
        plt.text(t1,f(t1) , k, color='green', fontsize=k*2 + 10)
        k += 1
        return Next_t(t1)


Next_t(t0)

def printFunc(f, a, b):
    t = np.arange(a, b, 0.01)
    s = f(t)
    plt.plot(t, s)
    plt.show()

printFunc(f,t0,t0+0.5)

