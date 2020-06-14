import numpy as np
import matplotlib.pyplot as plt
import parsing
import display
import normalization
import gradient_descent
import math

# ===================== Initialization =====================
Normalize = True
Debug_gradient = False
Display_graph = True
Display_predictions = False

thetas = parsing.read_thetas()
raw_dataX, raw_dataY = parsing.read_data()

# ===================== Start output =====================
display.start_of_program_output(thetas, gradient_descent.cost(raw_dataX, raw_dataY, thetas[1], thetas[0]))

# ===================== Normalizing =====================
dataX, dataY, thetas = normalization.process_data(raw_dataX, raw_dataY, thetas, Normalize)

# =======================================
# =======================================
# =======================================
# =======================================

# # Getting current thetas values
# thetas = parsing.read_thetas()
# print(thetas)

# # Getting dataset
# dataX, dataY = parsing.read_data()

x, y = np.array(dataX), np.array(dataY)
x, y = x.reshape(x.shape[0], 1), y.reshape(y.shape[0], 1)
# print("shapes = " + str(x.shape) + "    " + str(y.shape))

X = np.hstack((x, np.ones(x.shape)))
Y = y
# print(X)

theta = np.array(thetas)
theta = theta.reshape(theta.shape[0], 1)
# print(theta)
# print("shape = " + str(theta.shape))

def model(X, theta):
    return X.dot(theta)

def cost_function(X, Y, theta):
    m = len(Y)
    s = (1 / (2 * m)) * np.sum((model(X, theta) - Y)**2)
    return s

def gradient(X, Y, theta):
    m = len(Y)
    return (1 / m) * X.T.dot(model(X, theta) - Y)

def gradient_descent(X, Y, theta, learning_rate, iterations):
    for i in range(iterations):
        theta = theta - learning_rate * gradient(X, Y, theta)
    return theta

new_theta = gradient_descent(X, Y, theta, learning_rate = 0.000000000015, iterations = 500)

print("Model :")
print(model(X, theta))
print("cost = " + str(cost_function(X, y, theta)))
print("new_theta = " + str(new_theta))

#============================
#============================
#============================

# ===================== Denormalizing =====================
thetas = normalization.get_final_thetas(raw_dataX, raw_dataY, [new_theta[0][0], new_theta[1][0]], Normalize)

# ===================== End output =====================
display.end_of_program_output(thetas, gradient_descent.cost(raw_dataX, raw_dataY, thetas[1], thetas[0]), raw_dataX, Display_predictions)


# ===================== Writing new thetas to file =====================
parsing.write_thetas(thetas)



# # Saving new thetas values to file
# parsing.write_thetas([new_theta[0][0], new_theta[1][0]])