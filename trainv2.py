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
m = len(dataX)

# Saving new thetas values to file
parsing.write_thetas(thetas)