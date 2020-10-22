import numpy as np
import matplotlib.pyplot as plt
import pylab
import statistics as stat

DataSetxi = [1, 3, 2, 5, 7, 7]
DataSetyi = [1, 4, 7, 8, 12, 13]

fig, ax = plt.subplots()


class regression:
    @staticmethod
    def sumMaltipy(mx, my):
        sum = 0
        for i in range(len(mx)):
            sum += mx[i] * my[i]
        return sum

    @staticmethod
    def sumSquare(mx):
        sum = 0
        for i in range(len(mx)):
            sum += mx[i] * mx[i]
        return sum

    @staticmethod
    def linear_predict(x):
        N = len(DataSetxi)
        w1 = (regression.sumMaltipy(DataSetxi, DataSetyi) - stat.mean(DataSetxi) * stat.mean(DataSetyi) * N) / \
             (regression.sumSquare(DataSetxi) - N * stat.mean(DataSetxi) * stat.mean(DataSetxi))
        w0 = stat.mean(DataSetyi) - w1 * stat.mean(DataSetxi)
        y = w1 * x + w0
        print("x is ", x, "predict y is ", y)

    @staticmethod
    def liner_plot(mx, my):
        N = len(mx)
        w1 = (regression.sumMaltipy(mx, my) - stat.mean(mx) * stat.mean(my) * N) / \
             (regression.sumSquare(mx) - N * stat.mean(mx) * stat.mean(mx))
        w0 = stat.mean(my) - w1 * stat.mean(mx)
        x = np.linspace(min(mx) - 1, max(mx) + 2)
        y = w1 * x + w0
        ax.grid(axis='both')
        plt.title(label='regression')
        ax.plot(x, y)
        #ax.plot(mx, my, 'ro')

    @staticmethod
    def data_plot(mx ,my):
        ax.grid(axis='both')
        plt.title(label='reg')
        ax.plot(mx, my, 'ro')

    @staticmethod
    def liner_plot2(mx, my):
        N = len(mx)
        w1 = stat.mean(mx) / stat.mean(my)
        w0 = stat.mean(my) - w1 * stat.mean(mx)
        x = np.linspace(min(mx) - 1, max(mx) + 2)
        y = w1 * x +w0
        ax.grid(axis='both')
        plt.title(label='regression')
        ax.plot(x, y, color='lightgray')
        #ax.plot(mx, my, 'ro')  #dataplot

regression.liner_plot(DataSetxi, DataSetyi)
regression.data_plot(DataSetxi, DataSetyi)
regression.liner_plot2(DataSetxi, DataSetyi)
pylab.show()
