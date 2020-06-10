import matplotlib.pyplot as plt

def display_predictions(thetas, dataX):
    for i in range(len(dataX)):
        p = thetas[0] + thetas[1] * dataX[i]
        print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))
    print("")

def end_of_program_output(thetas, iterations, cost, dataX, show_predictions):
    print("Finished " + str(iterations) + " iterations !\n")
    if (show_predictions == True):
        display_predictions(thetas, dataX)
    print("Final t0 = " + str(thetas[0]))
    print("Final t1 = " + str(thetas[1]))
    print("Cost = " + str(cost))