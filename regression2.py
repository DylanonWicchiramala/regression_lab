import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

fig, ax = plt.subplots()
plt.grid(axis='both')

DataSetxi = np.array([0, 13, 22, 34, 52, 59, 76])
DataSetyi = np.array([100, 99, 87, 88, 71, 83, 78])


def data_plot(mx, my, color='black'):
    plt.title(label='Regression')
    plt.scatter(mx, my, color=color)


def regression_plot(mx, my, degree=1, color=None):
    mx = mx.reshape((-1, 1))
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(mx)
    mx_ = transformer.transform(mx)
    # mx_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(mx)
    model = LinearRegression().fit(mx_, my)  # calculate weight value
    M = 5
    x = np.linspace(min(mx) - M, max(mx) + M)
    data_plot(mx, my)
    ax.plot(x, model.predict(transformer.transform(x)), color=color)


def regrassion_predict(val, tx=DataSetxi, ty=DataSetyi, degree=1):
    tx = tx.reshape((-1, 1))
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(tx)
    tx_ = transformer.transform(tx)
    # mx_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(mx)
    model = LinearRegression().fit(tx_, ty)  # calculate weight value
    print("x is ", val, "predict y is ", *model.predict(transformer.transform(np.array(val).reshape(-1, 1))))

regression_plot(DataSetxi, DataSetyi, 2, 'lightblue')
regression_plot(DataSetxi, DataSetyi, 3, 'blue')
regression_plot(DataSetxi, DataSetyi, 4, 'darkblue')

pylab.show()
