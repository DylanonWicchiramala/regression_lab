import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat
import math
import sum

DataSetxi = [0, 13, 22, 34, 52, 59, 76]
DataSetyi = [100, 96, 94, 91, 86, 83, 78]

fig, ax = plt.subplots()


def linear_predict(val, tx=DataSetxi, ty=DataSetyi, axis=None):
    N = len(tx)
    w1 = (sum.maltipy(tx, ty) - stat.mean(tx) * stat.mean(ty) * N) / \
         (sum.square(tx) - N * math.pow(stat.mean(tx), 2))
    w0 = stat.mean(DataSetyi) - w1 * stat.mean(tx)
    if axis == 'x' or axis is None:
        y = w1 * val + w0
        print("x is ", val, "predict y is ", y)
        return y
    elif axis == 'y':
        x = (val - w0) / w1
        print("y is ", val, "predict x is", x)
        return x

def liner_plot(mx, my):
    N = len(mx)
    w1 = (sum.maltipy(mx, my) - stat.mean(mx) * stat.mean(my) * N) / \
         (sum.square(mx) - N * math.pow(stat.mean(mx), 2))
    w0 = stat.mean(my) - w1 * stat.mean(mx)
    x = np.linspace(min(mx) - 1, max(mx) + 2)
    y = w1 * x + w0
    # ax.grid(axis='both')
    plt.title(label='regression')
    ax.plot(x, y)
    # ax.plot(mx, my, 'ro')

def data_plot(mx, my):
    # ax.grid(axis='both')
    plt.title(label='reg')
    plt.scatter(mx, my, color='black')


ax.grid(axis='both')

liner_plot(DataSetxi, DataSetyi)
data_plot(DataSetxi, DataSetyi)
print(linear_predict(0, axis='y') / 60, "hrs.")
pylab.show()
