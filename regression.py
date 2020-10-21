import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat


def sumMaltipy(mx, my):
    sum = 0
    for i in range(len(mx)):
        sum += mx[i] * my[i]
    return sum


def sumSquare(mx):
    sum = 0
    for i in range(len(mx)):
        sum += mx[i] * mx[i]
    return sum


def plot_liner_regression(mx, my):
    N = len(mx)
    w1 = (sumMaltipy(mx, my) - stat.mean(mx) * stat.mean(my) * N) / (sumSquare(mx) - N * stat.mean(mx) * stat.mean(mx))
    w0 = stat.mean(my) - w1 * stat.mean(mx)
    x = np.linspace(min(mx) - 1, max(mx) + 2)
    y = (w1 * x) + w0
    fig, ax = plt.subplots()
    ax.grid(axis='both')
    plt.title(label='regression')
    ax.plot(x, y)
    ax.plot(mx, my, 'ro')


DataSetxi = [1, 2, 3, 5, 7, 7]
DataSetyi = [1, 4, 7, 8, 12, 13]

plot_liner_regression(DataSetxi, DataSetyi)
pylab.show()
