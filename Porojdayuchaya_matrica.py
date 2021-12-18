""" n>k
G - порождающая матрица (k*n)
S - случайная невырожденная матрица (k*k)
P - случайная матрица перестановок (n*n)
G` - S*G*P (k*n)
V - кодовое слово
m - сообщение в виде последовательностей двоичных символов длины k
z - случайный вектор длины n
"""

import random
from data import *
import numpy as np
from numpy import linalg


def random_vec_z():
    z = []
    for i in range(7):
        a = random.randint(0, 1)
        z.append(a)
    print(z)
    return z


def random_transposition_matrix():  # S
    S = []
    for i in range(4):
        b = []
        for j in range(4):
            x = random.randint(0, 1)
            b.append(x)
        S.append(b)
    S = np.array(S)
    return S


def not_float():  # для любых матриц - не забывай вставлять в функцию
    S = random_transposition_matrix()
    i = 0
    while np.linalg.det(S) == 0.0:
        S = random_transposition_matrix()
        i += 1
    else:
        print('Number of attempts to create a correct random permutation matrix - ', i)
        # S = inverse_matrix_rtm_func(S)
        # S = refactor_matrix_or_list(S)
        return S


def random_nondegenerate_matrix():  # P
    P = []
    for i in range(7):
        b = []
        for j in range(7):
            x = random.randint(0, 1)
            b.append(x)
        P.append(b)
    P = np.array(P)
    return P


def inverse_matrix_rnm_func(*args):  # P^-1
    args = random_nondegenerate_matrix()
    print(args, type(args))
    # args = args[0]
    inverse_matrix_rnm = linalg.inv(args)
    print(inverse_matrix_rnm)
    # inverse_matrix_rnm = refactor_matrix_or_list(inverse_matrix_rnm)
    return inverse_matrix_rnm


random_nondegenerate_matrix() #
inverse_matrix_rnm_func() # остановился на отладке кода с нот флоат


# def code_word():
#     V = U.dot(G)


def refactor_matrix_or_list(*args):
    args = args[0]
    args_ = []
    if type(args[0]) == np.ndarray:
        for i in range(len(args)):
            args__ = []
            for j in range(len(args[i])):
                int_value = args[i][j].astype(int)
                if int_value == 0:
                    args__.append(int_value)
                elif int_value % 2 == 0:
                    int_value = 0
                    args__.append(int_value)
                else:
                    int_value = 1
                    args__.append(int_value)
            args_.append(args__)
        return args_
    elif type(args[0]) == np.int32:
        for i in range(len(args)):
            args__ = []
            if args[i] == 0:
                args__.append(args[i])
            elif args[i] % 2 == 0:
                args[i] = 0
                args__.append(args[i])
            else:
                args[i] = 1
                args__.append(args[i])
            args_.append(args__)
        return args_


def to_list(*args):  # превращает матрицу n*1 в матрицу 1*n
    args = args[0]
    args_ = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            args_.append(args[i][j])
    return args_


def caclulation_un_g():  # ^G = S*G*P
    P = np.array(random_nondegenerate_matrix())
    S = np.array(random_transposition_matrix())
    un_G = S.dot(G)  # умножение матриц G * S
    un_G = np.array(refactor_matrix_or_list(un_G))  # заполнение матрицы бинарными числами
    un_G = un_G.dot(P)
    un_G = np.array(refactor_matrix_or_list(un_G))
    return un_G


def open_key_func():  # (^G, t)
    open_key = []
    t = 1
    open_key.append(caclulation_un_g())
    open_key.append(t)


def changed_message_func():  # c` = m*^G + z
    changed_message_text = m.dot(caclulation_un_g())
    changed_message_text = refactor_matrix_or_list(changed_message_text)
    changed_message_text = changed_message_text + z
    return changed_message_text


def c_by_c_and_p():  # c^ = (m*S)*G + z*P^-1
    ms = np.array(m.dot(
        random_transposition_matrix()))  # сделать коректный вывод, пустить через функция преобразования в 0 1 из 3 2 5
    msg = ms.dot(G)
    msg = to_list(refactor_matrix_or_list(
        msg))  # меняет матрицу из [0 1 2 1 2 3 4] и [[1], [0], [1], [1], [0], [1], [0]] в [0, 1, 0, 1, 0, 1, 0]
    zp = z.dot(inverse_matrix_rnm_func())
    print(zp)

# open_key_func()
# random_transposition_matrix()
# c_by_c_and_p()
