import numpy as np
import random

global k, n, t, G
k = 4
n = 7
t = 1

G_revers = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1],
                     [1, 1, 0, 1],
                     [1, 0, 1, 1],
                     [0, 1, 1, 1]])  # not correct

G = np.array([[1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 0, 1],  # здесь ощибка! 0 1 0 0 1 0 0 в последней единице
              [0, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1]])  # correct


def random_error_vector():
    rand = random.randint(0, 6)
    z = []
    for i in range(n):
        if i == rand:
            x = [1]
        else:
            x = [0]
        z.append(x)
    z = np.array(z)
    return z


def random_non_degenerate_matrix_func():  # S
    S = np.array([[1, 1, 0, 1],
                  [1, 0, 0, 1],
                  [0, 1, 1, 1],
                  [1, 1, 0, 0]])
    return S


def random_transposition_matrix_func():  # P
    P = np.array([[0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 1, 0, 0]])
    return P
