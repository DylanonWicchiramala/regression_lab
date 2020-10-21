import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat

DataSetxi = [1, 3, 2, 5, 7, 7]
DataSetyi = [1, 4, 7, 8, 12, 13]

fig, ax = plt.subplots()


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


def liner_regression(mx, my):
    N = len(mx)
    w1 = (sumMaltipy(mx, my) - stat.mean(mx) * stat.mean(my) * N) / (sumSquare(mx) - N * stat.mean(mx) * stat.mean(mx))
    w0 = stat.mean(my) - w1 * stat.mean(mx)
    x = np.linspace(min(mx) - 1, max(mx) + 2)
    return w1 * x + w0


def predict_liner_regression(x):
    N = len(DataSetxi)
    w1 = (sumMaltipy(DataSetxi, DataSetyi) - stat.mean(DataSetxi) * stat.mean(DataSetyi) * N) / (
                sumSquare(DataSetxi) - N * stat.mean(DataSetxi) * stat.mean(DataSetxi))
    w0 = stat.mean(DataSetyi) - w1 * stat.mean(DataSetxi)
    y = w1 * x + w0
    print("x is ", x, "predict y is ", y)


def plot_liner_regression(mx, my):
    y = liner_regression(mx, my)
    x = np.linspace(min(mx) - 1, max(mx) + 2)
    ax.grid(axis='both')
    plt.title(label='regression')
    ax.plot(x, y)
    ax.plot(mx, my, 'ro')


plot_liner_regression(DataSetxi, DataSetyi)
predict_liner_regression(12)
pylab.show()
