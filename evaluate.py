import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

def plot_residuals(x, y, yhat):
'''
Takes in a feature and target variable and predictions for the target variable based on the linear regression model. It displays a 
plot of the baseline model residuals and a plot of the linear regression model residuals.

Arguments:  x - the feature variable with which the linear regression model was made in order to make a prediction for the target variable 
            y - the target variable's actual datapoints
            yhat - the predicted datapoints for the target variable by the linear regression model
'''

    residual = yhat - y
    baseline_residual = y.mean() - y

    plt.figure(figsize = (11,5))

    plt.subplot(121)
    plt.scatter(x, baseline_residual)
    plt.axhline(y = 0, ls = '-', color = "#FF5E13")
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('Baseline Residuals')

    plt.subplot(122)
    plt.scatter(x, residual)
    plt.axhline(y = 0, ls = '-', color = "#FF5E13")
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('OLS model residuals')

def regression_errors(y, yhat):
    '''
    Function that takes in a target variable and target variable predictions made by a linear regression model. It prints out the 
    following information:
            Sum of squared errors
            Explained sum of squares
            Total sum of squares
            Mean squared error
            Root mean squared error

    Arguments:  y - the actual datapoints of a target variable
                yhat - the predicted datapoints of a target variable made by a linear regression model
    '''
    MSE = mean_squared_error(y, yhat)
    SSE = MSE * len(y)
    RMSE = mean_squared_error(y, yhat, squared = False)
    ESS = sum((yhat - y.mean())**2)
    TSS = ESS + SSE

    return SSE, ESS, TSS, MSE, RMSE

def baseline_mean_errors(y):
    baseline = pd.Series(y.mean()).repeat(len(y))
    MSE = mean_squared_error(y, baseline)
    SSE = MSE * len(y)
    RMSE = mean_squared_error(y, baseline, squared = False)

    return MSE, SSE, RMSE

def better_than_baseline(y, yhat):
    '''
    Returns: returns true if the model performs better than the baseline, otherwise false
    '''
    model_SSE, model_ESS, model_TSS, model_MSE, model_RMSE = regression_errors(y, yhat)
    baseline_MSE, baseline_SSE, baseline_RMSE = baseline_mean_errors(y)

    return (model_SSE - baseline_MSE) > 0