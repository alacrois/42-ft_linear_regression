# import csv
data = []
f = open('data.csv', 'r')
lines = f.read().split('\n')
f.close()
for i in range(1, len(lines)):
    line = lines[i]
    if len(line.split(",")) > 1 :
        data.append([line.split(",")[0], line.split(",")[1].strip("\n")])
for i in range(len(data)):
    # print("data " + str(i) + " = " + str(data[i]))
    print("data " + str(i) + " ===> km = " + str(data[i][0]) + "  price = " + str(data[i][1]))

