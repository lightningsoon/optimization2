import math
import numpy as np
import matplotlib.pyplot as plt
Epsilon=1e-3#极限

y=lambda t:t*(t+2)#函数

(a,b)=[-3,5]# 确定a,b

Belta=(3-math.sqrt(5))/2
t2=a+Belta*(b-a)
y2=y(t2)

while True:
    t1=a+b-t2
    y1=y(t1)
    if abs(t1-t2)<Epsilon:
        t_ = (t1 + t2) / 2
        y_ = y(t_)
        print('t*=%f,y*=%f' % (t_, y_))
        break
    else:
        while abs(t1-t2)>=Epsilon:
            if y1<y2:
                a=t2
                t2=t1
                y2=y1
                break
            else:
                b=t1
                t1=t2
                y1=y2
                t2=a+Belta*(b-a)
                y2=y(t2)

        if abs(t1 - t2) < Epsilon:
            t_ = (t1 + t2) / 2
            y_ = y(t_)
            print('t*=%f,y*=%f' % (t_, y_))
            break


#绘制函数图像

def printFunc(f, a, b, x, y):
    t = np.arange(a, b, 0.01)
    s = f(t)
    plt.plot(t, s)
    plt.plot([x], [y], 'ro')
    plt.text(x,y,'(%0.3f,%0.3f)'%(x,y), color='red', fontsize=10)
    plt.show()

printFunc(y,a,b,t_,y_)