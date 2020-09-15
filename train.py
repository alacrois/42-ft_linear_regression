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
Adjust_learning_rate = True
learning_rate = 0.1 if Normalize == True else 0.000000000015
iterations = 500

# Parsing :
thetas = parsing.read_thetas()
raw_dataX, raw_dataY = parsing.read_data()
dataX, dataY, thetas = normalization.process_data(raw_dataX, raw_dataY, thetas, Normalize)

# Formating new variables :
x, y = np.array(dataX), np.array(dataY)
x, y = x.reshape(x.shape[0], 1), y.reshape(y.shape[0], 1)
X = np.hstack((x, np.ones(x.shape)))
Y = y
thetas.reverse()
theta = np.array(thetas)
theta = theta.reshape(theta.shape[0], 1)

# ===================== Start output =====================
display.start_output(raw_dataX, raw_dataY, X, Y, theta, Normalize)

# ===================== Gradient descent =====================
theta, prediction_history = gradient_descent.gradient_descent(X, Y, theta, learning_rate, \
                                iterations, Debug_gradient, Adjust_learning_rate)

# ===================== Data graph =====================
display.display_graph(dataX, dataY, prediction_history, Display_graph)

# ===================== Denormalizing =====================
X, Y, final_theta = normalization.denormalize(raw_dataX, raw_dataY, X, Y, theta, Normalize)

# ===================== End output =====================
display.end_output(final_theta, gradient_descent.cost_function(X, Y, final_theta), X, Display_predictions)

# ===================== Writing new thetas to file =====================
parsing.write_thetas([final_theta[1][0], final_theta[0][0]])
