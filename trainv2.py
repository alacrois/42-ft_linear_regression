import numpy as np
import functions
import parsing
import matplotlib.pyplot as plt
import math

# Getting current thetas values
thetas = parsing.read_thetas()
print(thetas)

# Getting dataset
dataX, dataY = parsing.read_data()
x, y = np.array(dataX), np.array(dataY)
x, y = x.reshape(x.shape[0], 1), y.reshape(y.shape[0], 1)
print("shapes = " + str(x.shape) + "    " + str(y.shape))

X = np.hstack((x, np.ones(x.shape)))
print(X)

theta = np.array(thetas)
theta = theta.reshape(theta.shape[0], 1)
print(theta)
print("shape = " + str(theta.shape))

m = len(dataX)

# Saving new thetas values to file
parsing.write_thetas(thetas)