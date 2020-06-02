import matplotlib.pyplot as plt

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

learningRatio = 0.1
f = open('data.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
        data.append([line.split(",")[0], line.split(",")[1].strip("\n")])
        dataX.append(float(line.split(",")[0]))
        dataY.append(float(line.split(",")[1]))

# born ?
minY = min(dataY)
maxY = max(dataY)
minX = min(dataX)
maxX = max(dataX)
dataX_normalized = []
dataY_normalized = []
for i in range(len(data)):
    dataX_normalized.append((dataX[i] - minX) / (maxX - minX))
    dataY_normalized.append((dataY[i] - minY) / (maxY - minY))

def cost(a, b):
    error = 0
    for i in range(len(data)):
        #old :
        km = float(data[i][0])
        p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]

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
        km = float(data[i][0])
        p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]

        s += km * ((a * km + b) - p)
    s = s / len(data)
    return s

def der_cost_b(a, b):
    s = 0
    for i in range(len(data)):
        #old :
        km = float(data[i][0])
        p = float(data[i][1])
        #new :
        # km = dataX[i]
        # p = dataY[i]

        s += ((a * km + b) - p)
    s = s / len(data)
    return s

iterations = 500
# tmp_t0 = t0
# tmp_t1 = t1

# t0 = 10000
# t1 = -0.03

print("Starting...  t0 = " + str(t0) + "  t1 = " + str(t1) + "\n")
print("cost(t1, t0) = " + str(cost(t1, t0)) + "\n")


# learning_rate = 0.000000000015
learning_rate = 0.0000000001
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

predictions = []
for i in range(len(dataX)) :
    predictions.append(t0 + t1 * dataX[i])
plt.scatter(dataX, dataY)
plt.scatter(dataX_normalized, dataY_normalized)
plt.plot(dataX, predictions, c='r')
plt.show()
print("Finished " + str(iterations) + " iterations ! ==> t0 = " + str(t0) + "  t1 = " + str(t1))

# for i in range(len(data)):
#     print("dataX[" + str(i) + "] = " + str(dataX[i]))
#     print("dataY[" + str(i) + "] = " + str(dataY[i]))
# print("min(dataX) = " + str(min(dataX)))