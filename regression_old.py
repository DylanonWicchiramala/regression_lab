import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat
import math

DataSetxi = []          #[0, 13, 22, 34, 52, 59, 76]       
DataSetyi = []          #[100, 96, 94, 91, 86, 83, 78]

fig, ax = plt.subplots()

def maltipy(mx, my):
    sum: int = 0
    for i in range(len(mx)):
        sum += mx[i] * my[i]
    return sum

def square(mx):
    sum: int = 0
    for i in range(len(mx)):
        sum += mx[i] * mx[i]
    return sum


def linear_predict(val, trainingSetX=DataSetxi, trainingSetY=DataSetyi, axis=None):
    N = len(trainingSetX)
    w1 = (sum.maltipy(trainingSetX, trainingSetY) - stat.mean(trainingSetX) * stat.mean(trainingSetY) * N) / \
         (sum.square(trainingSetX) - N * math.pow(stat.mean(trainingSetX), 2))
    w0 = stat.mean(DataSetyi) - w1 * stat.mean(trainingSetX)
    if axis == 'x' or axis is None:
        y = w1 * val + w0
        print("x is ", val, "predict y is ", y)
        return y
    elif axis == 'y':
        x = (val - w0) / w1
        print("y is ", val, "predict x is", x)
        return x


def data_plot(mx, my):
    # ax.grid(axis='both')
    #plt.title(label='reg')
    plt.scatter(mx, my, color='black')


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
    data_plot(mx,my)
    # ax.plot(mx, my, 'ro')



ax.grid(axis='both')

#liner_plot(DataSetxi, DataSetyi)
#data_plot(DataSetxi, DataSetyi)
#linear_predict(0, axis='y')

#pylab.show()
#always use "pylab.show()" after called plot-function