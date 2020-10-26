import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

fig, ax = plt.subplots()
plt.grid(axis='both')

DataSetxi = np.array([0, 13, 22, 34, 52, 59, 76]).reshape((-1, 1))
DataSetyi = np.array([100, 96, 94, 91, 86, 83, 78])


def data_plot(mx, my):
    plt.title(label='Regression')
    plt.scatter(mx, my, color='black')


def regression_plot(mx, my, degree=None):
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(mx)
    mx_ = transformer.transform(mx)
    #mx_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(mx)
    model = LinearRegression().fit(mx_, my)  # calculate weight value
    x = np.linspace(min(mx), max(my))
    data_plot(mx, my)
    ax.plot(x, model.predict(transformer.transform(x)))


regression_plot(DataSetxi, DataSetyi, 2)

pylab.show()
