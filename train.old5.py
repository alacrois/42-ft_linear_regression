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

# ===================== Gradient descent =====================
thetas, prediction_history = gradient_descent.gradient_descent(thetas, dataX, dataY, Debug_gradient, Normalize)

# ===================== Data graph =====================
display.display_graph(dataX, dataY, prediction_history, Display_graph)

# ===================== Denormalizing =====================
thetas = normalization.get_final_thetas(raw_dataX, raw_dataY, thetas, Normalize)

# ===================== End output =====================
display.end_of_program_output(thetas, gradient_descent.cost(raw_dataX, raw_dataY, thetas[1], thetas[0]), raw_dataX, Display_predictions)

# ===================== Writing new thetas to file =====================
parsing.write_thetas(thetas)