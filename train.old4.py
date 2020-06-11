import matplotlib.pyplot as plt
import parsing
import display
import normalization
import math

# ===================== Parsing data =====================
# f = open('thetas', 'r')
# lines = f.read().split('\n')
# f.close()
# t0 = float(lines[0])
# t1 = float(lines[1])
t = parsing.read_thetas()


# dataX = []
# dataY = []

# f = open('data.csv', 'r')
# lines = f.read().split('\n')
# f.close()
# for i in range(1, len(lines)):
#     line = lines[i]
#     if len(line.split(",")) > 1 :
#         dataX.append(float(line.split(",")[0]))
#         dataY.append(float(line.split(",")[1]))
Normalize = True
raw_dataX, raw_dataY = parsing.read_data()
dataX, dataY, t = normalization.process_data(raw_dataX, raw_dataY, t, Normalize)

t0 = t[0]
t1 = t[1]

# ===================== Functions =====================
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

def debug_gradient_values(dca, dcb, c, i):
    print("Iteration " + str(i) + " : cost = " + str(c) + " & t0 = " + str(t0) + " & t1 = " + str(t1) + \
            " & dca = " + str(dca) + " & dcb = " + str(dcb))

def slow_learning(learning_rate):
    return learning_rate * 0.1

def speed_up_learning(learning_rate):
    return learning_rate * 1.05

# ===================== Initialization =====================
# normalize = True
display_p = True
display_g = True
debug_gradient = True
adjust_learning_rate = True
starting_cost = cost(dataX, dataY, t1, t0)
# dataX_range = max(dataX) - min(dataX)
# dataY_range = max(dataY) - min(dataY)
# if (normalize == True):
#     normalize_data(dataX_range, dataY_range)
cost_history = []
cost_history_size = 3
all_predictions = []
iterations = 500
# Best learning rate for raw data (not normalized) :
# learning_rate = 0.000000000015
# learning_rate = 0.0000000001
# learning_rate = 0.0001
learning_rate = 0.1

print("starting t0 = " + str(t0) + "\nstarting t1 = " + str(t1))
print("cost(t1, t0) = " + str(starting_cost) + "\n")

# ===================== Gradient descent =====================
for iteration in range(iterations):
    tmp_t = t
    # tmp_t[0] = t[0]
    # tmp_t[1] = t[1]
    dca = der_cost_a(dataX, dataY, tmp_t[1], tmp_t[0])
    dcb = der_cost_b(dataX, dataY, tmp_t[1], tmp_t[0])
    t[1] = t[1] - learning_rate * dca
    t[0] = t[0] - learning_rate * dcb
    # t[1] = learning_rate * dca
    # t[0] = learning_rate * dcb

    c = cost(dataX, dataY, t[1], t[0])
    if adjust_learning_rate == True :
        # cost_history.insert(0, cost(t[1], t[0]))
        cost_history.insert(0, c)
        while len(cost_history) > cost_history_size :
            cost_history.pop()
    if adjust_learning_rate == True and iteration >= cost_history_size and len(cost_history) > 1:
        cost_is_increasing = True
        # print("Debug : ")
        for i in range(0, len(cost_history) - 1) :
            if cost_history[i] <= cost_history[i + 1] :
                cost_is_increasing = False
                break
        if cost_is_increasing == True :
            print("Learning rate slowed at i " + str(iteration) + " ! (len(ch) = " + str(len(cost_history)) + ")  lr = " + str(learning_rate))
            learning_rate = slow_learning(learning_rate)
            t[1] = tmp_t[1]
            t[0] = tmp_t[0]
            cost_history.clear()
        else :
            learning_rate = speed_up_learning(learning_rate)

    if debug_gradient == True:
        # debug_gradient_values(dca, dcb, cost(t[1], t[0]), iteration)
        debug_gradient_values(dca, dcb, c, iteration)

    if iteration == 0 or iteration == int(iterations**0.5) or iteration == iterations - 1:
        all_predictions.append(get_prediction_history_for_graph(t[0], t[1]))


# ===================== Data graph =====================
# plt.plot(dataX, predictions, c='r')
if display_g == True:
    plt.scatter(dataX, dataY, c='k')
    plt.plot(dataX, all_predictions[0], c='r')
    plt.plot(dataX, all_predictions[1], c='y')
    plt.plot(dataX, all_predictions[2], c='g')
    plt.show()

# ===================== Denormalizing =====================
# if normalize == True:
    # t0 = t0 * (dataY_range)
    # t1 = t1 * (dataY_range / dataX_range)
    # denormalize_data(dataX_range, dataY_range)
t = normalization.get_final_thetas(raw_dataX, raw_dataY, t, Normalize)

# ===================== Displaying some infos =====================
display.end_of_program_output(t, iterations, cost(raw_dataX, raw_dataY, t[1], t[0]), raw_dataX, display_p)


# ===================== Writing new thetas to file =====================
parsing.write_thetas(t)