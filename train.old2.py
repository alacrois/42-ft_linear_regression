import matplotlib.pyplot as plt
import math

# Parsing data...
f = open('thetas', 'r')
lines = f.read().split('\n')
f.close()
t0 = float(lines[0])
t1 = float(lines[1])

def pe(km):
    return t0 + t1 * km

data = []
dataX = []
dataY = []

f = open('data.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
        data.append([line.split(",")[0], line.split(",")[1].strip("\n")])
        dataX.append(float(line.split(",")[0]))
        dataY.append(float(line.split(",")[1]))

# Normalizing data...
minY = min(dataY)
maxY = max(dataY)
minX = min(dataX)
maxX = max(dataX)
dataX_range = maxX - minX
dataY_range = maxY - minY
dataX_normalized = []
dataY_normalized = []
for i in range(len(data)):
    dataX_normalized.append(dataX[i] / dataX_range)
    dataY_normalized.append(dataY[i] / dataY_range)
    # dataX_normalized.append((dataX[i] - minX) / (maxX - minX))
    # dataY_normalized.append((dataY[i] - minY) / (maxY - minY))

# Some functions...
def cost(a, b):
    error = 0
    for i in range(len(data)):
        #old :
        # km = float(data[i][0])
        # p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]

        # print(str(i) + " : km(x) = " + str(km) + " & p(y) = " + str(p))
        error += ((a * km + b) - p)**2
        # error += p - (a + b * km)
    error = error / (len(data) * 2)
    # print("len(data) = " + str(len(data)))
    return error

def der_cost_a(a, b):
    s = 0
    for i in range(len(data)):
        #old :
        # km = float(data[i][0])
        # p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]

        s += km * ((a * km + b) - p)
    s = s / len(data)
    return s

def der_cost_b(a, b):
    s = 0
    for i in range(len(data)):
        #old :
        # km = float(data[i][0])
        # p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]

        s += ((a * km + b) - p)
    s = s / len(data)
    return s

def get_predictions(tmp_t0, tmp_t1) :
    predictions = []
    for i in range(len(dataX)) :
        # predictions.append(tmp_t0 + tmp_t1 * dataX[i])
        predictions.append(tmp_t0 + tmp_t1 * dataX_normalized[i])
    return predictions

all_predictions = []

iterations = 500
# tmp_t0 = t0
# tmp_t1 = t1

# t0 = 10000
# t1 = -0.03

t0 = 0
t1 = 0

print("Starting...  t0 = " + str(t0) + "  t1 = " + str(t1) + "\n")
print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")

# learning_rate = 0.000000000015
# learning_rate = 0.0000000001
learning_rate = 0.5
for every in range(iterations):
    tmp_t0 = t0
    tmp_t1 = t1
    print("der_cost_a(tmp_t1, tmp_t0) = " + str(der_cost_a(tmp_t1, tmp_t0)))
    print("der_cost_b(tmp_t1, tmp_t0) = " + str(der_cost_b(tmp_t1, tmp_t0)))
    t1 = t1 - learning_rate * der_cost_a(tmp_t1, tmp_t0)
    t0 = t0 - learning_rate * der_cost_b(tmp_t1, tmp_t0)
    # t0 = tmp_t0
    # t1 = tmp_t1
    print("One iterations done ==> t0 = " + str(t0) + " & t1 = " + str(t1))
    print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")
    # learning_rate = learning_rate / 2
    if every == 0 or every == int(iterations / 4) or every == iterations - 1:
        all_predictions.append(get_predictions(t0, t1))


# plt.scatter(dataX, dataY, c='k')
plt.scatter(dataX_normalized, dataY_normalized, c='k')
# plt.plot(dataX, predictions, c='r')
plt.scatter(dataX_normalized, all_predictions[0], c='r')
plt.scatter(dataX_normalized, all_predictions[1], c='b')
plt.scatter(dataX_normalized, all_predictions[2], c='g')
plt.show()
print("Finished " + str(iterations) + " iterations ! ==> t0 = " + str(t0) + "  t1 = " + str(t1))

# Denormalizing... :
t0_final = t0 * (dataY_range)
t1_final = t1 * (dataY_range / dataX_range)

print("t0_corrected = " + str(t0_corrected))
print("t1_corrected = " + str(t1_corrected))

for i in range(len(dataX)):
    p = t0_corrected + t1_corrected * dataX[i]
    print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))
# for i in range(len(data)):
#     print("dataX[" + str(i) + "] = " + str(dataX[i]))
#     print("dataY[" + str(i) + "] = " + str(dataY[i]))
# print("min(dataX) = " + str(min(dataX)))