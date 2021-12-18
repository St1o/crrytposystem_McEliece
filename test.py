import numpy as np

x = np. array([[1.0, 1.0, 1.0, 1.0],
               [1.0, 0.0, 0.0, 1.0],
               [1.0, 0.0, 1.0, 1.0],
               [0.0, 0.0, 0.0, 1.0]])

y = np.array([[1, 0, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1],
              [1, 1, 0, 1]])


for i in range(len(x)):
    x_ = []
    for j in range(len(x[i])):
        x[i][j] = x[i][j].astype(int)
        print('x[i][j] - ', type(x[i][j]))
        a = x[i][j]
        a = a.astype(int)
        print(a)
        print('a - ', type(a))

# for i in range(len(y)):
#     y_ = []
#     for j in range(len(y[i])):
#         print(type(y[i][j]))
#         print(y[i][j])