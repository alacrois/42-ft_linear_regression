import matplotlib.pyplot as plt

def display_predictions(thetas, dataX):
    for i in range(len(dataX)):
        p = thetas[0] + thetas[1] * dataX[i]
        print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))
    print("")

def start_of_program_output(t, c):
    print("Starting t0 = " + str(t[0]) + "\nStarting t1 = " + str(t[1]))
    print("Cost = " + str(c) + "\n")

def end_of_program_output(thetas, cost, dataX, Display_predictions):
    print("Finished gradient descent !\n")
    if (Display_predictions == True):
        display_predictions(thetas, dataX)
    print("Final t0 = " + str(thetas[0]))
    print("Final t1 = " + str(thetas[1]))
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