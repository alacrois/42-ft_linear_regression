import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def init(m, n):
    mat = np.random.randn(m, n)
    o = np.ones((m, 1))
    # o = o.reshape((o.shape[0], 1))
    result = np.hstack((mat, o))
    return result

if False:
    a = init(3, 5)
    face = misc.face(gray=True)
    y = face.shape[0]
    x = face.shape[1]
    ystart = int(y * 0.25)
    yend = int(y * 0.75)
    xstart = int(x * 0.25)
    xend = int(x * 0.75)
    newface = face[ystart:yend, xstart:xend]
    newface[newface < 100] = 0
    newface[newface > 150] = 255
    plt.imshow(newface, cmap=plt.cm.gray)
    plt.show()
    print(newface.shape)

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
    f.write(str(thetas[0]) + "\n" + str(thetas[1]) + "\n")
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