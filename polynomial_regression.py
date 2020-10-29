import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pylab

fig, ax = plt.subplots()
plt.grid(axis='both')

DataSetxi = np.array([])               #np.array([0, 13, 22, 34, 52, 59, 76])#
DataSetyi = np.array([])               #np.array([100, 99, 87, 88, 71, 83, 78])#

used_degree:int = 1
is_ploted:bool = False

#plot a data point (plot DataSetXi and DataSetYi)
# f(mx:numpy.array[training set; x axis] , my:numpy.array[training set; y axis] , color:str):void 
def data_plot(mx=DataSetxi, my=DataSetyi, color='black'):
    is_ploted = True
    plt.title(label='Regression')
    plt.scatter(mx, my, color=color)


#plot regression grapth.
# f(mx:numpy.array[training set; x axis] , my:numpy.array[training set; y axis] , \
# degree:int[dregree of polynomial regrassion] , color:str):void 
def regression_plot(mx = DataSetxi, my = DataSetyi, degree = 1, color = None):
    used_degree = degree
    is_ploted = True
    mx = mx.reshape((-1, 1))
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(mx)
    mx_ = transformer.transform(mx)
    # mx_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(mx)
    model = LinearRegression().fit(mx_, my)  # calculate weight value
    M = 5
    x = np.linspace(min(mx) - M, max(mx) + M)
    data_plot(mx, my)
    ax.plot(x, model.predict(transformer.transform(x)), color=color)


#predict value from regrassionfunction [regf(val_x)]
# f(val_x:float or int[value (x axis)], trainingSetX:numpy.array[training set; x axis] ,
# trainingSetY:numpy.array[training set; y axis] , degree:int[dregree of polynomial-regrassion-function-
# that want to predict. defualt is last used dregree] , color:str):float[predicted value (y axis)]
def regrassion_predict(val_x, trainingSetX = DataSetxi, trainingSetY = DataSetyi, degree = used_degree):
    trainingSetX = trainingSetX.reshape((-1, 1))
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(trainingSetX)
    tx_ = transformer.transform(trainingSetX)
    # mx_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(mx)
    model = LinearRegression().fit(tx_, trainingSetY)  # calculate weight value
    print("x is ", val_x, "predict y is ", *model.predict(transformer.transform(np.array(val_x).reshape(-1, 1))))
    return float(model.predict(transformer.transform(np.array(val_x).reshape(-1, 1))))


#regression_plot(DataSetxi, DataSetyi, 2, 'lightblue')
#regression_plot(DataSetxi, DataSetyi, 3, 'blue')
#regression_plot(4, 'darkblue')
#print(regrassion_predict(82))

if is_ploted : pylab.show