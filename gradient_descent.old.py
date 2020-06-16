import display

def cost(dataX, dataY, a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += ((a * km + b) - p)**2
    s = s / (len(dataX) * 2)
    return s

def der_cost_a(dataX, dataY, a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += km * ((a * km + b) - p)
    s = s / len(dataX)
    return s

def der_cost_b(dataX, dataY, a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += ((a * km + b) - p)
    s = s / len(dataX)
    return s

def get_prediction_history_for_graph(tmp_t0, tmp_t1, dataX):
    predictions = []
    for i in range(len(dataX)) :
        predictions.append(tmp_t0 + tmp_t1 * dataX[i])
    return predictions

def slow_learning(learning_rate):
    return learning_rate * 0.1

def speed_up_learning(learning_rate):
    return learning_rate * 1.05

def gradient_descent(t, dataX, dataY, Debug_gradient, Normalize):
    adjust_learning_rate = True
    cost_history = []
    cost_history_size = 3
    all_predictions = []
    iterations = 500
    if Normalize == True:
        learning_rate = 0.1
    else:
        learning_rate = 0.000000000015
    for iteration in range(iterations):
        tmp_t = t
        dca = der_cost_a(dataX, dataY, tmp_t[1], tmp_t[0])
        dcb = der_cost_b(dataX, dataY, tmp_t[1], tmp_t[0])
        t[1] = t[1] - learning_rate * dca
        t[0] = t[0] - learning_rate * dcb

        c = cost(dataX, dataY, t[1], t[0])
        if adjust_learning_rate == True :
            cost_history.insert(0, c)
            while len(cost_history) > cost_history_size :
                cost_history.pop()
        if adjust_learning_rate == True and iteration >= cost_history_size and len(cost_history) > 1:
            cost_is_increasing = True
            for i in range(0, len(cost_history) - 1) :
                if cost_history[i] <= cost_history[i + 1] :
                    cost_is_increasing = False
                    break
            if cost_is_increasing == True :
                if Debug_gradient == True:
                    print("Learning rate slowed at i " + str(iteration) + " ! (len(ch) = " + str(len(cost_history)) + ")  lr = " + str(learning_rate))
                learning_rate = slow_learning(learning_rate)
                t[1] = tmp_t[1]
                t[0] = tmp_t[0]
                cost_history.clear()
            else :
                learning_rate = speed_up_learning(learning_rate)

        if Debug_gradient == True:
            display.debug_gradient_values(dca, dcb, c, iteration, t)

        if iteration == 0 or iteration == int(iterations**0.5) or iteration == iterations - 1:
            all_predictions.append(get_prediction_history_for_graph(t[0], t[1], dataX))
    return t, all_predictions