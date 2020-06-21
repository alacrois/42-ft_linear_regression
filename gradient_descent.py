import numpy as np

def model(X, theta):
    return X.dot(theta)

def cost_function(X, Y, theta):
    # print("X = " + str(X) + "\nY = " + str(Y) + "\ntheta = " + str(theta))
    m = float(len(Y))
    s = (1 / (2 * m)) * np.sum((model(X, theta) - Y)**2)
    return s

def gradient(X, Y, theta):
    m = float(len(Y))
    return (1 / m) * X.T.dot(model(X, theta) - Y)

def slow_learning(learning_rate):
    return learning_rate * 0.1

def speed_up_learning(learning_rate):
    return learning_rate * 1.05

def adjust_learning_rate(learning_rate, X, Y, theta, previous_theta, cost_history, iteration, Debug_gradient):
    cost_history_size = 3
    c = cost_function(X, Y, theta)
    cost_history.insert(0, c)
    while len(cost_history) > cost_history_size :
        cost_history.pop()
    if iteration >= cost_history_size and len(cost_history) > 1:
        cost_is_increasing = True
        for i in range(0, len(cost_history) - 1) :
            if cost_history[i] <= cost_history[i + 1] :
                cost_is_increasing = False
                break
        if cost_is_increasing == True :
            if Debug_gradient == True:
                print("Learning rate slowed at iteration " + str(iteration) + " ! (len(ch) = " + str(len(cost_history)) + ")  lr = " + str(learning_rate))
            learning_rate = slow_learning(learning_rate)
            theta = previous_theta
            del cost_history[:]
        else :
            learning_rate = speed_up_learning(learning_rate)
    return learning_rate, theta, cost_history

def gradient_descent(X, Y, theta, learning_rate, iterations, Debug_gradient, Adjust_learning_rate):
    prediction_history = []
    cost_history = []
    for it in range(iterations):
        previous_theta = theta
        theta = theta - learning_rate * gradient(X, Y, theta)
        if it == 0 or it == int(iterations**0.5) or it == iterations - 1:
            prediction_history.append(model(X, theta))
        if Adjust_learning_rate == True:
            learning_rate, theta, cost_history = adjust_learning_rate(learning_rate, X, Y, theta, \
                                                    previous_theta, cost_history, it, Debug_gradient)
    return theta, prediction_history