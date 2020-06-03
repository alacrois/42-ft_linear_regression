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

dataX = []
dataY = []

f = open('data2.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
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
for i in range(len(dataX)):
    dataX_normalized.append(dataX[i] / dataX_range)
    dataY_normalized.append(dataY[i] / dataY_range)
    # dataX_normalized.append((dataX[i] - minX) / (maxX - minX))
    # dataY_normalized.append((dataY[i] - minY) / (maxY - minY))

# Some functions...
def cost(a, b):
    s = 0
    for i in range(len(dataX)):
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]
        s += ((a * km + b) - p)**2
    s = s / (len(dataX) * 2)
    return s

def der_cost_a(a, b):
    s = 0
    for i in range(len(dataX)):
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]

        s += km * ((a * km + b) - p)
    s = s / len(dataX)
    return s

def der_cost_b(a, b):
    s = 0
    for i in range(len(dataX)):
        # km = dataX[i]
        # p = dataY[i]
        km = dataX_normalized[i]
        p = dataY_normalized[i]

        s += ((a * km + b) - p)
    s = s / len(dataX)
    return s

def get_predictions(tmp_t0, tmp_t1, denormalize) :
    if denormalize == True :
        tmp_t0 = tmp_t0 * (dataY_range)
        tmp_t1 = tmp_t1 * (dataY_range / dataX_range)
    predictions = []
    for i in range(len(dataX)) :
        if denormalize == True :
            predictions.append(tmp_t0 + tmp_t1 * dataX[i])
        else :
            predictions.append(tmp_t0 + tmp_t1 * dataX_normalized[i])
    return predictions

all_predictions = []

iterations = 500
# tmp_t0 = t0
# tmp_t1 = t1

# t0 = 10000
# t1 = -0.03

# t0 = 0
# t1 = 0

print("Starting...  t0 = " + str(t0) + "  t1 = " + str(t1) + "\n")
print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")

# learning_rate = 0.000000000015
# learning_rate = 0.0000000001
learning_rate = 0.5
for every in range(iterations):
    tmp_t0 = t0
    tmp_t1 = t1
    # print("der_cost_a(tmp_t1, tmp_t0) = " + str(der_cost_a(tmp_t1, tmp_t0)))
    # print("der_cost_b(tmp_t1, tmp_t0) = " + str(der_cost_b(tmp_t1, tmp_t0)))
    t1 = t1 - learning_rate * der_cost_a(tmp_t1, tmp_t0)
    t0 = t0 - learning_rate * der_cost_b(tmp_t1, tmp_t0)
    # print("One iterations done ==> t0 = " + str(t0) + " & t1 = " + str(t1))
    # print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")
    if every == 0 or every == int(iterations / 4) or every == iterations - 1:
        all_predictions.append(get_predictions(t0, t1, False))


# plt.scatter(dataX, dataY, c='k')
# plt.plot(dataX, predictions, c='r')

plt.scatter(dataX_normalized, dataY_normalized, c='k')
plt.scatter(dataX_normalized, all_predictions[0], c='r')
plt.scatter(dataX_normalized, all_predictions[1], c='b')
plt.scatter(dataX_normalized, all_predictions[2], c='g')

# plt.scatter(dataX, dataY, c='k')
# plt.scatter(dataX, all_predictions[0], c='r')
# plt.scatter(dataX, all_predictions[1], c='b')
# plt.scatter(dataX, all_predictions[2], c='g')


plt.show()
print("Finished " + str(iterations) + " iterations ! ==> t0 = " + str(t0) + "  t1 = " + str(t1))

# Denormalizing... :
t0_final = t0 * (dataY_range)
t1_final = t1 * (dataY_range / dataX_range)

print("t0_final = " + str(t0_final))
print("t1_final = " + str(t1_final))

for i in range(len(dataX)):
    p = t0_final + t1_final * dataX[i]
    print("dataX[" + str(i) + "] = " + str(dataX[i]) + " & prediction = " + str(p))

# Writing new thetas to file...
f = open('thetas', 'w')
f.write(str(t0_final) + "\n" + str(t1_final) + "\n")
f.close()