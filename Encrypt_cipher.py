# -*- coding: utf-8 -*-

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

# import numpy as np
import time

from data_wiki import *


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


def public_key_func():  # (^G, t)
    public_key = []
    public_key.append(to_list(caclulation_un_g()))
    public_key.append(t)
    return public_key


def received_message_func(m):  # c` = m*^G + z
    ciphred_message_text = m.dot(
        caclulation_un_g())  # здесь происходит кодирование сообщение, т.е. взаимодействует сообщение и ^G
    ciphred_message_text = refactor_matrix_or_list(ciphred_message_text)
    # print('Ciphred message text: ', np.array(to_list(ciphred_message_text)))
    received_message_text = ciphred_message_text + random_error_vector()  # добавляется ошибка
    return received_message_text


def c_plus_pi(received_message, inverse_random_transposition_matrix):
    cp = received_message.dot(inverse_random_transposition_matrix)
    return cp


def encrypted(correction_message, inverse_random_non_degenerate_matrix):
    new_cp = []
    for i in range(k):
        new_cp.append(correction_message[i])
    new_cp = np.array(new_cp)
    new_cp = np.array(to_list(refactor_matrix_or_list(new_cp.dot(inverse_random_non_degenerate_matrix))))  # m*S^-1
    print('result', new_cp)


def write_message(received_message):
    message_file = open('Message.txt', 'a')  # a - дозапись, w - перезапись
    message_file.write(str(received_message))
    # message_file.write(str()
    message_file.close()


def write_public_keys():
    public_key_file = open('Public Keys.txt', 'a')
    public_key_file.write(str(public_key_func()))  # тут должна быть переменная, а не функция
    public_key_file.close()


def write_privat_keys(random_non_degenerate_matrix, random_transposition_matrix, matrix_g):
    privat_key_file = open('Privat Keys.txt', 'a')
    privat_key_file.write(str(random_non_degenerate_matrix))
    privat_key_file.write(str(random_transposition_matrix))
    privat_key_file.write(str(matrix_g))
    privat_key_file.write('-')
    privat_key_file.close()


def preparation_encrypt_procedure(m):
    # создание матриц

    random_transposition_matrix = random_transposition_matrix_func()  # checking_null_determinate_matrix(1)
    random_non_degenerate_matrix = random_non_degenerate_matrix_func()  # checking_null_determinate_matrix(0)
    # print(to_list(random_non_degenerate_matrix))
    matrix_g = G

    # формировка текста

    # отправка матриц и текста в алгоритм (сам алгоритм) - received_message_func()
    received_message = np.array(to_list(refactor_matrix_or_list(received_message_func(m))))

    # запись по файлам
    write_message(received_message)
    write_public_keys()
    write_privat_keys(to_list(random_non_degenerate_matrix), to_list(random_transposition_matrix), to_list(matrix_g))


def create_abstract_text(filename):
    start_time = time.time()
    if filename.lower().endswith('.txt'):
        f = open(filename, 'rb')
        text = f.read()
        f.close()
        f = open('binary_text.txt', 'w')
        a = "".join(format(i, "08b") for i in text)
        print(a)
        f.write(str(a))
        f.close()
    else:
        f = open(filename, 'rb')
        text = f.read()
        print(len(text), text)
        f.close()
        string_binary = ''
        for i in range(len(text)):
            a = int(text[i])
            binary = bin(a)[2:]
            if len(binary) % 8 == 0:
                string_binary += binary
            else:
                binary = (8 - (len(binary) % 8)) * '0' + binary
                string_binary += binary
        print(len(string_binary), string_binary)
        f = open('binary_text.txt', 'w')
        f.write(str(string_binary))
        f.close()
        a = string_binary

    clear_file = open('Message.txt', 'w')
    clear_file.close()
    clear_file = open('Public Keys.txt', 'w')
    clear_file.close()
    clear_file = open('Privat Keys.txt', 'w')
    clear_file.close()

    create_code_word()
    time_work = " %s seconds" % (time.time() - start_time)
    a = f'Message:\n{a}\nMessage is encrypt and send\nPublic keys are send\nPrivat keys are send\nRunning time: {time_work}'
    return a


def create_code_word():
    f_binary = open('binary_text.txt', 'r')
    full_text = f_binary.read()
    f_binary.close()
    while (len(full_text)) % k != 0:
        full_text += '0'
    while len(full_text) != 0:
        word = full_text[0:4]
        w = []
        for i in range(len(word)):
            w.append(int(word[i]))
        m = np.array(w)
        preparation_encrypt_procedure(m)
        full_text = full_text[4:]

# create_abstract_text()
