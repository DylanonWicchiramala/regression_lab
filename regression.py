import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat
from regression_lab.Sum import Sum

DataSetxi = [10, 23, 32, 44, 62, 69, 86]
DataSetyi = [100, 96, 94, 91, 86, 83, 78]

fig, ax = plt.subplots()

class regression:

    @staticmethod
    def linear_predict(val, axis=None):
        N = len(DataSetxi)
        w1 = (Sum.maltipy(DataSetxi, DataSetyi) - stat.mean(DataSetxi) * stat.mean(DataSetyi) * N) / \
             (Sum.square(DataSetxi) - N * stat.mean(DataSetxi) * stat.mean(DataSetxi))
        w0 = stat.mean(DataSetyi) - w1 * stat.mean(DataSetxi)

        if (axis == 'x' or axis is None):
            y = w1 * val + w0
            print("x is ", val, "predict y is ", y)
            return y
        elif (axis == 'y'):
            x = (val - w0) / w1
            print("y is ", val, "predict x is", x)
            return x

    @staticmethod
    def liner_plot(mx, my):
        N = len(mx)
        w1 = (Sum.maltipy(mx, my) - stat.mean(mx) * stat.mean(my) * N) / \
             (Sum.square(mx) - N * stat.mean(mx) * stat.mean(mx))
        w0 = stat.mean(my) - w1 * stat.mean(mx)
        x = np.linspace(min(mx) - 1, max(mx) + 2)
        y = w1 * x + w0
        # ax.grid(axis='both')
        plt.title(label='regression')
        ax.plot(x, y)
        # ax.plot(mx, my, 'ro')

    @staticmethod
    def data_plot(mx, my):
        # ax.grid(axis='both')
        plt.title(label='reg')
        ax.plot(mx, my, 'ro')


ax.grid(axis='both')

regression.liner_plot(DataSetxi, DataSetyi)
regression.data_plot(DataSetxi, DataSetyi)
print(regression.linear_predict(0, axis='y')/60, "hrs.")
pylab.show()
