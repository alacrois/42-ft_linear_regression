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
        # print(str(i) + " : km(x) = " + str(km) + " & p(y) = " + str(p))
        error += ((a * km + b) - p)**2
        # error += p - (a + b * km)
    error = error / (len(data) * 2)
    # print("len(data) = " + str(len(data)))
    return error

def der_cost_a(a, b):
    s = 0
    for i in range(len(data)):
        km = float(data[i][0])
        p = float(data[i][1])
        s += km * ((a * km + b) - p)
    s = s / len(data)
    return s

def der_cost_b(a, b):
    s = 0
    for i in range(len(data)):
        km = float(data[i][0])
        p = float(data[i][1])
        s += ((a * km + b) - p)
    s = s / len(data)
    return s

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
# ratio = 0.1
# prevC = cost(t0, t1)
# for i in range(len(data)):
# for every in range(iterations):
    # s1 = 0
    # s2 = 0
    # for i in range(len(data)):
    #     km = float(data[i][0])
    #     p = float(data[i][1])
    #     s1 += (tmpt0 + tmpt1 * km) - p
    #     s2 += ((tmpt0 + tmpt1 * km) - p) * km
    # print("s1 = " + str(s1) + "  s2 = " + str(s2))
    # tmpt0 = tmpt0 - ratio * (s1 / len(data)) 
    # tmpt1 = tmpt1 - ratio * (s2 / len(data))
iterations = 2
tmp_t0 = t0
tmp_t1 = t1
# tmp_t0 = 1
# tmp_t1 = 1
print("Starting...  t0 = " + str(t0) + "  t1 = " + str(t1) + "\n")

learning_rate = 0.00001
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
    print("cost(t1, t0) = " + str(cost(t0, t1)) + "\n")
    # learning_rate = learning_rate / 2


print("Finished " + str(iterations) + " iterations ! ==> t0 = " + str(t0) + "  t1 = " + str(t1))