import numpy as np

# anchors = [10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326]
# for i in range(0, len(anchors), 2):
#   print(anchors[i] * anchors[i + 1])


x = [5.890625,  3.453125, 27.21875,  14.21875,   4.671875, 11.171875,  7.3125,   18.484375,  8.9375]
y = [6.5,       3.859375, 29.046875, 15.234375,  5.078125, 11.78125,   8.125,    20.109375,  9.75 ]
area = []

for i in range(len(x)):
    area.append(x[i] * y[i])

print(area)
print(np.argsort(area))

new_x = [0 for _ in range(len(x))]
new_y = [0 for _ in range(len(y))]

for i in range(len(np.argsort(area))):
    new_x[i] = int(x[np.argsort(area)[i]])
    new_y[i] = int(y[np.argsort(area)[i]])

anchors = []
for i in range(len(new_x)):
	anchors.append(new_x[i])
	anchors.append(new_y[i])

print(anchors)


for i in range(len(new_x)):
    print(new_x[i] * new_y[i])
