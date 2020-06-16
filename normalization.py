import numpy as np

def process_data(raw_dataX, raw_dataY, raw_thetas, normalize):
    if normalize == False:
        return raw_dataX, raw_dataY, raw_thetas
    dataX_range = max(raw_dataX) - min(raw_dataX)
    dataY_range = max(raw_dataY) - min(raw_dataY)
    thetas = [raw_thetas[0] / dataY_range, \
                raw_thetas[1] / (dataY_range / dataX_range)]
    dataX, dataY = [], []
    for i in range(len(raw_dataX)):
        dataX.append(raw_dataX[i] / dataX_range)
        dataY.append(raw_dataY[i] / dataY_range)
    return dataX, dataY, thetas

def denormalize(raw_dataX, raw_dataY, X, Y, theta, normalize):
    if normalize == False:
        return X, Y, theta
    dataX_range = max(raw_dataX) - min(raw_dataX)
    dataY_range = max(raw_dataY) - min(raw_dataY)
    theta[0][0] = theta[0][0] * (dataY_range / dataX_range)
    theta[1][0] = theta[1][0] * dataY_range
    X[:,0] = X[:,0] * dataX_range
    Y = Y * dataY_range
    return X, Y, theta