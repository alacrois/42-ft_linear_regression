# def normalize_data(dataX_range, dataY_range):
#     global t0, t1, dataX, dataY
#     t0 = t0 / (dataY_range)
#     t1 = t1 / (dataY_range / dataX_range)
#     for i in range(len(dataX)):
#         dataX[i] = dataX[i] / dataX_range
#         dataY[i] = dataY[i] / dataY_range

def process_data(raw_dataX, raw_dataY, raw_thetas, normalize):
    if normalize == False:
        return raw_dataX, raw_dataY, raw_thetas
    dataX_range = max(raw_dataX) - min(raw_dataX)
    dataY_range = max(raw_dataY) - min(raw_dataY)
    thetas = [raw_thetas[0] / dataY_range, \
                raw_thetas[1] / (dataY_range / dataX_range)]
    # t0 = t0 / (dataY_range)
    # t1 = t1 / (dataY_range / dataX_range)
    dataX, dataY = [], []
    for i in range(len(raw_dataX)):
        dataX.append(raw_dataX[i] / dataX_range)
        dataY.append(raw_dataY[i] / dataY_range)
        # dataX[i] = dataX[i] / dataX_range
        # dataY[i] = dataY[i] / dataY_range
    return dataX, dataY, thetas

def get_final_thetas(raw_dataX, raw_dataY, thetas, normalize):
    if normalize == False:
        return thetas
    dataX_range = max(raw_dataX) - min(raw_dataX)
    dataY_range = max(raw_dataY) - min(raw_dataY)
    final_thetas = [thetas[0] * dataY_range, \
                    thetas[1] * (dataY_range / dataX_range)]
    return final_thetas

def denormalize_data(dataX_range, dataY_range):
    global t0, t1, dataX, dataY
    t0 = t0 * (dataY_range)
    t1 = t1 * (dataY_range / dataX_range)
    for i in range(len(dataX)):
        dataX[i] = dataX[i] * dataX_range
        dataY[i] = dataY[i] * dataY_range