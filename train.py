import matplotlib.pyplot as plt
import math

# ===================== Parsing data =====================
f = open('thetas', 'r')
lines = f.read().split('\n')
f.close()
t0 = float(lines[0])
t1 = float(lines[1])

dataX = []
dataY = []

f = open('data.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
        dataX.append(float(line.split(",")[0]))
        dataY.append(float(line.split(",")[1]))

# ===================== Functions =====================
def cost(a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += ((a * km + b) - p)**2
    s = s / (len(dataX) * 2)
    return s

def der_cost_a(a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += km * ((a * km + b) - p)
    s = s / len(dataX)
    return s

def der_cost_b(a, b):
    s = 0
    for i in range(len(dataX)):
        km = dataX[i]
        p = dataY[i]
        s += ((a * km + b) - p)
    s = s / len(dataX)
    return s

def get_prediction_history_for_graph(tmp_t0, tmp_t1):
    predictions = []
    for i in range(len(dataX)) :
        predictions.append(tmp_t0 + tmp_t1 * dataX[i])
    return predictions

def display_predictions(t0, t1):
    for i in range(len(dataX)):
        p = t0 + t1 * dataX[i]
        print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))
    print("")

def normalize_data(dataX_range, dataY_range):
    for i in range(len(dataX)):
        dataX[i] = dataX[i] / dataX_range
        dataY[i] = dataY[i] / dataY_range

def denormalize_data(dataX_range, dataY_range):
    for i in range(len(dataX)):
        dataX[i] = dataX[i] * dataX_range
        dataY[i] = dataY[i] * dataY_range

def debug_gradient_values(dca, dcb, c, i):
    print("Iteration " + str(i) + " : cost = " + str(c) + " & dca = " + str(dca) + " & dcb = " + str(dcb))

# ===================== Initialization =====================
normalize = True
display_p = False
display_g = False
debug_gradient = True
starting_cost = cost(t1, t0)
dataX_range = max(dataX) - min(dataX)
dataY_range = max(dataY) - min(dataY)
if (normalize == True):
    normalize_data(dataX_range, dataY_range)
all_predictions = []
iterations = 500
# learning_rate = 0.000000000015
# learning_rate = 0.0000000001
# learning_rate = 0.0001
learning_rate = 0.5

print("starting t0 = " + str(t0) + "\nstarting t1 = " + str(t1))
print("cost(t1, t0) = " + str(starting_cost) + "\n")

# ===================== Gradient descent =====================
for every in range(iterations):
    tmp_t0 = t0
    tmp_t1 = t1
    t1 = t1 - learning_rate * der_cost_a(tmp_t1, tmp_t0)
    t0 = t0 - learning_rate * der_cost_b(tmp_t1, tmp_t0)
    if debug_gradient == True:
        debug_gradient_values(der_cost_a(tmp_t1, tmp_t0), der_cost_b(tmp_t1, tmp_t0), cost(t1, t0), every)
    # print("der_cost_a(tmp_t1, tmp_t0) = " + str(der_cost_a(tmp_t1, tmp_t0)))
    # print("der_cost_b(tmp_t1, tmp_t0) = " + str(der_cost_b(tmp_t1, tmp_t0)))
    # print("One iterations done ==> t0 = " + str(t0) + " & t1 = " + str(t1))
    # print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")
    if every == 1 or every == int(iterations**0.5) or every == iterations - 1:
        all_predictions.append(get_prediction_history_for_graph(t0, t1))


# ===================== Data graph =====================
# plt.plot(dataX, predictions, c='r')
if display_g == True:
    plt.scatter(dataX, dataY, c='k')
    plt.plot(dataX, all_predictions[0], c='r')
    plt.plot(dataX, all_predictions[1], c='y')
    plt.plot(dataX, all_predictions[2], c='g')
    plt.show()

# ===================== Denormalizing =====================
if normalize == True:
    t0 = t0 * (dataY_range)
    t1 = t1 * (dataY_range / dataX_range)
    denormalize_data(dataX_range, dataY_range)

# ===================== Displaying some infos =====================
print("Finished " + str(iterations) + " iterations !\n")
if (display_p == True):
    display_predictions(t0, t1)
print("final t0 = " + str(t0))
print("final t1 = " + str(t1))
print("cost(t1, t0) = " + str(cost(t1, t0)))


# ===================== Writing new thetas to file =====================
f = open('thetas', 'w')
f.write(str(t0) + "\n" + str(t1) + "\n")
f.close()