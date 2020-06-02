f = open('thetas', 'r')
lines = f.read().split('\n')
f.close()
t0 = float(lines[0])
t1 = float(lines[1])

def pe(km):
    return t0 + t1 * km

data = []
learningRatio = 0.1
f = open('data.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
        data.append([line.split(",")[0], line.split(",")[1].strip("\n")])

def cost(a, b):
    error = 0
    for i in range(len(data)):
        km = float(data[i][0])
        p = float(data[i][1])
        # error += ((a + b * km) - p)**2
        error += p - (a + b * km)
    error = error / len(data)
    return error

# t0error = 0
# t1error = 0
# for i in range(len(data)):
#     # print("data " + str(i) + " = " + str(data[i]))
#     # print("data " + str(i) + " ===> km = " + str(data[i][0]) + "  price = " + str(data[i][1]))
#     km = float(data[i][0])
#     p = float(data[i][1])
#     t0error += pe(km) - p
#     t1error += (pe(km) - p) * km
#     tmpt0 = (learningRatio * -t0error) / (i + 1)
#     tmpt1 = (learningRatio * -t1error) / (i + 1)
#     # learningRatio *= 0.05
#     t0 = tmpt0
#     t1 = tmpt1
# # tmpt0 = (learningRatio * t0error) / len(data)
# # tmpt1 = (learningRatio * t1error) / len(data)
ratio = 0.1
prevC = cost(t0, t1)
# for i in range(len(data)):
tmpt0 = t0
tmpt1 = t1
for k in range(3):
    s1 = 0
    s2 = 0
    for i in range(len(data)):
        km = float(data[i][0])
        p = float(data[i][1])
        s1 += (tmpt0 + tmpt1 * km) - p
        s2 += ((tmpt0 + tmpt1 * km) - p) * km
    print("s1 = " + str(s1) + "  s2 = " + str(s2))
    tmpt0 = tmpt0 - ratio * (s1 / len(data)) 
    tmpt1 = tmpt1 - ratio * (s2 / len(data))


print("tmpt0 = " + str(tmpt0) + "  tmpt1 = " + str(tmpt1))