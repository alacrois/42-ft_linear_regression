import matplotlib.pyplot as plt
import normalization
import numpy as np
import gradient_descentv2 as gradient_descent

def display_predictions(thetas, dataX):
    for i in range(len(dataX)):
        p = thetas[0] + thetas[1] * dataX[i]
        print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))
    print("")

def start_of_program_output(t, c):
    print("Starting t0 = " + str(t[0]) + "\nStarting t1 = " + str(t[1]))
    print("Cost = " + str(c) + "\n")

# def model(X, theta):
#     return X.dot(theta)

# def cost_function(X, Y, theta):
#     m = len(Y)
#     s = (1 / (2 * m)) * np.sum((model(X, theta) - Y)**2)
#     return s

def start_output(raw_dataX, raw_dataY, X, Y, theta, Normalize):
    if Normalize == True:
        tmp_X, tmp_Y, t = normalization.denormalize(raw_dataX, raw_dataY, X.copy(), Y.copy(), theta.copy(), True)
        c = gradient_descent.cost_function(tmp_X, tmp_Y, t)
    else:
        c = gradient_descent.cost_function(X, Y, theta)
        t = theta
    print("Starting t0 = " + str(t[1][0]) + "\nStarting t1 = " + str(t[0][0]))
    # print("Cost = " + str(c * dataX_range * dataY_range) + "\n")
    print("Cost = " + str(c) + "\n")


def end_of_program_output(thetas, cost, dataX, Display_predictions):
    print("Finished gradient descent !\n")
    if (Display_predictions == True):
        display_predictions(thetas, dataX)
    print("Final t0 = " + str(thetas[0]))
    print("Final t1 = " + str(thetas[1]))
    print("Cost = " + str(cost))

def end_output(theta, cost, X, Display_predictions):
    print("Finished gradient descent !\n")
    if (Display_predictions == True):
        print("Model predictions :")
        print(X.dot(theta))
    print("\nFinal t0 = " + str(theta[1][0]))
    print("Final t1 = " + str(theta[0][0]))
    print("Cost = " + str(cost))

def debug_gradient_values(dca, dcb, c, i, t):
    print("Iteration " + str(i) + " : cost = " + str(c) + " & t[0] = " \
            + str(t[0]) + " & t[1] = " + str(t[1]) \
            + " & dca = " + str(dca) + " & dcb = " + str(dcb))

def display_graph(dataX, dataY, all_predictions, Display_graph):
    if Display_graph == True:
        # plt.plot(dataX, predictions, c='r')
        plt.scatter(dataX, dataY, c='k')
        plt.plot(dataX, all_predictions[0], c='r')
        plt.plot(dataX, all_predictions[1], c='y')
        plt.plot(dataX, all_predictions[2], c='g')
        plt.show()