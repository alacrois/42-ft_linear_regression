def normalize_data(dataX_range, dataY_range):
    global t0, t1, dataX, dataY
    t0 = t0 / (dataY_range)
    t1 = t1 / (dataY_range / dataX_range)
    for i in range(len(dataX)):
        dataX[i] = dataX[i] / dataX_range
        dataY[i] = dataY[i] / dataY_range

def denormalize_data(dataX_range, dataY_range):
    global t0, t1, dataX, dataY
    t0 = t0 * (dataY_range)
    t1 = t1 * (dataY_range / dataX_range)
    for i in range(len(dataX)):
        dataX[i] = dataX[i] * dataX_range
        dataY[i] = dataY[i] * dataY_range