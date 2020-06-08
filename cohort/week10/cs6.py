import numpy as np
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    x = bunchobject.data[:,np.newaxis,x_index]
    y = bunchobject.data[:,np.newaxis,y_index]
    poly = PolynomialFeatures(degree=order, include_bias=False)
    c_data = poly.fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(c_data, y, test_size=size, random_state=seed)
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    
    error = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results = {'coefficients': regr.coef_,
               'intercept': regr.intercept_,
               'mean squared error': error,
               'r2 score': r2}
    
    return x_train[:, [x_index]], y_train, x_test[:, [x_index]], y_pred, results