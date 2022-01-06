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
    return un_G


def open_key_func():  # (^G, t)
    open_key = []
    open_key.append(to_list(caclulation_un_g()))
    open_key.append(t)
    return open_key


def received_message_func():  # c` = m*^G + z
    ciphred_message_text = m.dot(
        caclulation_un_g())  # здесь происходит кодирование сообщение, т.е. взаимодействует сообщение и ^G
    ciphred_message_text = refactor_matrix_or_list(ciphred_message_text)
    print('a_ciphred_message_text: ', np.array(to_list(ciphred_message_text)))
    received_message_text = ciphred_message_text + z  # добавляется ошибка
    return received_message_text


def transposed_matrix_func():
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


def correction_syndrome(cp, transposed_matrix):
    syndrome = cp.dot(transposed_matrix)
    print('syndrome', np.array(to_list(refactor_matrix_or_list(syndrome))))
    return syndrome


def correction_message_func(syndrome, transposed_matrix, cp):
    for i in range(len(transposed_matrix)):
        if str(syndrome) == str(transposed_matrix[i]):
            error_position = i
            print(f'Ошибка была в {error_position + 1} позиции')
    correction_message = []
    i = 0
    while i < n:
        x = cp[i]
        if i == error_position:
            if cp[error_position] == 1:
                x = 0
            elif cp[error_position] == 0:
                x = 1
        correction_message.append(x)
        i += 1
    correction_message = np.array(correction_message)
    print('correction_message:', correction_message)
    return correction_message


def encrypted(correction_message, inverse_random_non_degenerate_matrix):
    new_cp = []
    for i in range(k):
        new_cp.append(correction_message[i])
    new_cp = np.array(new_cp)
    new_cp = np.array(to_list(refactor_matrix_or_list(new_cp.dot(inverse_random_non_degenerate_matrix))))  # m*S^-1
    print('result', new_cp)


def write_message(received_message):
    message_file = open('message.txt', 'a')  # a - дозапись, w - перезапись
    message_file.write(str(received_message))
    message_file.close()
    print('Message is encrypt and send')


def write_open_keys():
    open_key_file = open('open keys.txt', 'w')
    open_key_file.write(str(open_key_func()))
    open_key_file.close()
    print('Open keys are send')


# def write_close_keys():


def read_message():
    message_file = open('message.txt', 'r')
    string_text = message_file.read().split('][')
    print(string_text)
    int_text = []
    for i in range(len(string_text)):
        int_symbol = []
        for j in range(len(string_text[i])):
            if string_text[i][j] == '0':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] == '1':
                int_symbol.append(int(string_text[i][j]))
        int_text.append(int_symbol)
    receive_word = np.array(int_text[0])
    int_text.remove(int_text[0])  ###!!! оставить или удалить?
    print(int_text)
    return receive_word


def read_open_keys():
    open_key_file = open('open keys.txt', 'r')
    string_text = open_key_file.read().split('][')  # !!! УТОЧНИТЬ
    int_text = []
    print(string_text)
    for i in range(len(string_text)):
        int_symbol = []
        for j in range(len(string_text[i])):
            if string_text[i][j] == '0':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] == '1':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] != ']':
                t_variable = string_text[i][j + 1]
        int_text.append(int_symbol)
    int_text = int_text[0]
    int_text.pop()
    print(int_text)
    column = []
    l = 0
    for i in range(k):
        string = []
        for j in range(n):
            string.append(int_text[l])
            l += 1
        column.append(string)
    receive_open_key = np.array(column)
    # print(receive_open_key, t_variable)
    return receive_open_key


def create_encrypt_procedure():
    # создание матриц
    # формировка текста
    # отправка матриц в алгоритм
    # запись по файлам
    pass


def create_decrypt_procedure():
    # распаковка файлов
    message_text = 0
    open_key_text = 0
    close_key_text = 0
    while message_text is not None:
        message = message_text[0]
        open_key = open_key_text[0], open_key_text[1]
        close_key = close_key_text[0], close_key_text[1], close_key_text[2]
        # decrypt_algorithm(message)
        message_text.remove(message_text[0])
        open_key_text.remove(open_key_text[0], open_key_text[1])
        close_key_text.remove(close_key_text[0], close_key_text[1], close_key_text[2])
    # формирование общей картины текста


# def encrypt_algorithm():
#     random_transposition_matrix = random_transposition_matrix_func()  # checking_null_determinate_matrix(1)
#     random_non_degenerate_matrix = random_non_degenerate_matrix_func()  # checking_null_determinate_matrix(0)
#     received_message = np.array(to_list(refactor_matrix_or_list(received_message_func())))
#     # write(received_message)

def decrypt_algorithm():
    random_transposition_matrix = random_transposition_matrix_func()
    random_non_degenerate_matrix = random_non_degenerate_matrix_func()
    inverse_random_transposition_matrix = inverse_matrix_func(random_transposition_matrix)
    inverse_random_non_degenerate_matrix = inverse_matrix_func(random_non_degenerate_matrix)
    cp = c_plus_pi(read_message(), inverse_random_transposition_matrix)
    transposed_matrix = transposed_matrix_func()
    syndrome = np.array(to_list(refactor_matrix_or_list(correction_syndrome(cp, transposed_matrix))))
    correction_message = correction_message_func(syndrome, transposed_matrix, cp)
    # print('m^G + z = ', received_message, '- b_ciphred_message_text', '\ncp: ',
    #       cp)  # , '\nsyndrome: ',syndrome)#, '\ntransposed_matrix: \n', transposed_matrix)
    encrypted(correction_message, inverse_random_non_degenerate_matrix)


def mother_function():
    random_transposition_matrix = random_transposition_matrix_func()  # checking_null_determinate_matrix(1)
    random_non_degenerate_matrix = random_non_degenerate_matrix_func()  # checking_null_determinate_matrix(0)
    inverse_random_transposition_matrix = inverse_matrix_func(random_transposition_matrix)
    inverse_random_non_degenerate_matrix = inverse_matrix_func(random_non_degenerate_matrix)
    received_message = np.array(to_list(refactor_matrix_or_list(received_message_func())))
    # write(received_message)
    # read_open_keys()
    # read_message()
    decrypt_algorithm()
    # cp = c_plus_pi(read_message(), inverse_random_transposition_matrix)
    # transposed_matrix = transposed_matrix_func()
    # syndrome = np.array(to_list(refactor_matrix_or_list(correction_syndrome(cp, transposed_matrix))))
    # correction_message = correction_message_func(syndrome, transposed_matrix, cp)
    # print('m^G + z = ', received_message, '- b_ciphred_message_text', '\ncp: ',
    #       cp)  # , '\nsyndrome: ',syndrome)#, '\ntransposed_matrix: \n', transposed_matrix)
    # encrypted(correction_message, inverse_random_non_degenerate_matrix)


mother_function()
