import numpy as np

# Read thetas values from file
def read_thetas():
    f = open('thetas', 'r')
    lines = f.read().split('\n')
    f.close()
    t0 = float(lines[0])
    t1 = float(lines[1])
    return [t0, t1]

# Write thetas values to file
def write_thetas(thetas):
    f = open('thetas', 'w')
    f.write(str(thetas[0]) + "\n" + str(thetas[1]))
    f.close()

# Read dataset
def read_data():
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
    return dataX, dataY