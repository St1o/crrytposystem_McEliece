""" n>k
G - порождающая матрица (k*n)
S - случайная невырожденная матрица (k*k)
P - случайная матрица перестановок (n*n)
G` - S*G*P (k*n)
V - кодовое слово
m - сообщение в виде последовательностей двоичных символов длины k
z - случайный вектор длины n
Н^T - транспонированная матрица
"""

import random
from data_wiki import *
import numpy as np
from numpy import linalg


def random_vector_z_func():
    z = []
    for i in range(7):
        a = random.randint(0, 1)
        z.append(a)
    print(z)
    return z


# def random_non_degenerate_matrix_func():  # S random_non_degenerate_matrix_func
#     S = []
#     for i in range(4):
#         b = []
#         for j in range(4):
#             x = random.randint(0, 1)
#             b.append(x)
#         S.append(b)
#     S = np.array(S)
#     return S


# def random_transposition_matrix_func():  # P
#     P = []
#     for i in range(7):
#         b = []
#         for j in range(7):
#             x = random.randint(0, 1)
#             b.append(x)
#         P.append(b)
#     P = np.array(P)
#     return P


def inverse_matrix_func(*args):  # P^-1 or S^-1
    args = args[0]
    inverse_matrix = linalg.inv(args)
    inverse_matrix = refactor_matrix_or_list(inverse_matrix)
    return inverse_matrix


def checking_null_determinate_matrix(argument_of_function):  # для любой матрицы
    i = 0
    if argument_of_function == 1:
        random_transposition_matrix = random_transposition_matrix_func()
        if np.linalg.det(
                random_transposition_matrix) == 0.0:  # ПОКА МАТРИЦЫ СТАТИЧНЫЕ ОСТАВИТЬ ИФ, потом сделать ВАЙЛ, когда будут случайным образом задаваться
            random_transposition_matrix = random_transposition_matrix_func()
            i += 1
        else:
            print('Number of attempts to create a correct random permutation matrix - ', i)
            return random_transposition_matrix
    elif argument_of_function == 0:
        random_non_degenerate_matrix = random_non_degenerate_matrix_func()
        while np.linalg.det(random_non_degenerate_matrix) == 0.0:
            random_non_degenerate_matrix = random_non_degenerate_matrix_func()
            i += 1
        else:
            print('Number of attempts to create a correct random non degenerate matrix - ', i)
            return random_non_degenerate_matrix


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
        return np.array(args_)
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
        return np.array(args_)


def to_list(*args):  # превращает матрицу n*1 в матрицу 1*n
    args = args[0]
    args_ = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            args_.append(args[i][j])
    return args_


def caclulation_un_g():  # ^G = S*G*P
    S = np.array(random_non_degenerate_matrix_func())
    P = np.array(random_transposition_matrix_func())
    un_G = S.dot(G)  # умножение матриц S * G
    un_G = np.array(refactor_matrix_or_list(un_G))  # заполнение матрицы бинарными числами
    un_G = un_G.dot(P)
    un_G = np.array(refactor_matrix_or_list(un_G))
    print('G` :\n', un_G)
    return un_G


def open_key_func():  # (^G, t)
    open_key = []
    t = 1
    open_key.append(caclulation_un_g())
    open_key.append(t)


def received_message_func():  # c` = m*^G + z
    ciphred_message_text = m.dot(
        caclulation_un_g())  # здесь происходит кодирование сообщение, т.е. взаимодействует сообщение и ^G
    ciphred_message_text = refactor_matrix_or_list(ciphred_message_text)
    print('a_ciphred_message_text: ', np.array(to_list(ciphred_message_text)))
    received_message_text = ciphred_message_text + z  # добавляется ошибка
    return received_message_text


# def c_by_c_and_p(random_non_degenerate_matrix, inverse_random_transposition_matrix):  # c^ = (m*S)*G + z*P^-1
#     ms = np.array(m.dot(random_non_degenerate_matrix))
#     msg = ms.dot(G)
#     msg = to_list(refactor_matrix_or_list(
#         msg))  # меняет матрицу из [0 1 2 1 2 3 4] и [[1], [0], [1], [1], [0], [1], [0]] в [0, 1, 0, 1, 0, 1, 0]
#     zp = np.array(to_list(z)).dot(inverse_random_transposition_matrix)
#     zp = to_list(refactor_matrix_or_list(zp))
#     c_summ = to_list(refactor_matrix_or_list(np.array(msg) + np.array(zp)))
#     return c_summ


# def addition_c(c_summ, random_non_degenerate_matrix):
#     c_summ = np.array(c_summ)
#     random_non_degenerate_matrix = np.array(random_non_degenerate_matrix)
#     print(c_summ, random_non_degenerate_matrix)
#     new_m_summ = c_summ.dot(random_non_degenerate_matrix)
#     print(new_m_summ)


def transposed_matrix_func():
    # un_g = caclulation_un_g()
    # print('un_g', un_g, type(un_g))
    I = []
    Q = []

    for i in range(len(G)):
        I_ = []
        Q_ = []
        for j in range(len(G[i])):
            x = int(G[i][j])
            if j <= (len(G) - 1):
                I_.append(x)
            else:
                Q_.append(x)
        if type(I_[0]) == int:
            I.append(I_)
        else:
            pass
        if type(Q_[0]) == int:
            Q.append(Q_)
        else:
            pass

    I = np.array(I)
    Q = np.array(Q)

    QT = Q.transpose()
    range_j = j + 1
    range_i = j - i

    H = []
    l = 0
    for i in range(range_i):
        H_ = []
        k = 0
        for j in range(range_j):
            if j <= (len(QT[0]) - 1):
                H_.append(QT[i][j])
            elif j < range_j:
                H_.append(I[l][k])
                k += 1
        H.append(H_)
        l += 1

    H = np.array(H)
    H = H.transpose()
    return H


def c_plus_pi(received_message, inverse_random_transposition_matrix):
    cp = received_message.dot(inverse_random_transposition_matrix)
    return cp


# def correction_syndrome(cp, transposed_matrix):
#     syndrome = cp.dot(transposed_matrix)
#     return syndrome


def encrypted(cp, inverse_random_non_degenerate_matrix):
    # new_cp = np.array([1, 0, 0, 0])#, [1], [1], [0]])
    new_cp = []
    for i in range(k):
        new_cp.append(cp[i])
    new_cp = np.array(new_cp)
    print(new_cp)
    new = refactor_matrix_or_list(new_cp.dot(G)) # CP*G
    print('new', to_list(new))
    new_cp = new_cp.dot(inverse_random_non_degenerate_matrix)
    print('new_cp', new_cp)


    # new_cp = np.array([1, 0, 0, 0, 1, 1, 0])
    # new_cp = refactor_matrix_or_list(new_cp.dot(G.transpose()))
    # new_cp = new_cp.transpose().dot(inverse_random_non_degenerate_matrix)
    # print('new_cp: ', refactor_matrix_or_list(new_cp)[0])


def mother_function():
    random_transposition_matrix = random_transposition_matrix_func()  # checking_null_determinate_matrix(1)
    random_non_degenerate_matrix = random_non_degenerate_matrix_func()  # checking_null_determinate_matrix(0)
    inverse_random_transposition_matrix = inverse_matrix_func(random_transposition_matrix)
    print('inverse_random_transposition_matrix: \n', inverse_random_transposition_matrix)
    inverse_random_non_degenerate_matrix = inverse_matrix_func(random_non_degenerate_matrix)
    # c_summ = c_by_c_and_p(random_non_degenerate_matrix, inverse_random_transposition_matrix)
    received_message = np.array(to_list(refactor_matrix_or_list(received_message_func())))
    cp = c_plus_pi(received_message, inverse_random_transposition_matrix)
    transposed_matrix = transposed_matrix_func()
    # syndrome = to_list(refactor_matrix_or_list(correction_syndrome(cp, transposed_matrix)))
    print('m^G + z = ', received_message, '- b_ciphred_message_text', '\ncp: ', cp)#, '\nsyndrome: ',syndrome)#, '\ntransposed_matrix: \n', transposed_matrix)
    encrypted(cp, inverse_random_non_degenerate_matrix)


mother_function()
