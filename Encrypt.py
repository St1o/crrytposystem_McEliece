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

import time

from Data import *


def refactor_matrix_or_list(*args):  # превращает матрицу или столбец десятичной СС в двоичную СС
    value = args[0]
    updated_matrix_or_list = []

    if type(value[0]) == np.ndarray:  # для матриц
        for i in range(len(value)):
            line_value = []
            for j in range(len(value[i])):
                int_value = value[i][j].astype(int)
                if int_value == 0:
                    line_value.append(int_value)
                elif int_value % 2 == 0:
                    int_value = 0
                    line_value.append(int_value)
                else:
                    int_value = 1
                    line_value.append(int_value)
            updated_matrix_or_list.append(line_value)

        return np.array(updated_matrix_or_list)

    elif type(value[0]) == np.int32:  # для столбцов
        for i in range(len(value)):
            line_value = []
            if value[i] == 0:
                line_value.append(value[i])
            elif value[i] % 2 == 0:
                value[i] = 0
                line_value.append(value[i])
            else:
                value[i] = 1
                line_value.append(value[i])
            updated_matrix_or_list.append(line_value)

        return np.array(updated_matrix_or_list)


def to_list(*args):  # превращает матрицу n*1 в матрицу 1*n (столбец в строку)
    value = args[0]
    updated_list = []

    for i in range(len(value)):
        for j in range(len(value[i])):
            updated_list.append(value[i][j])

    return updated_list


def calculation_un_g():  # создание матрицы ^G = S*G*P
    matrix_s = np.array(checking_null_determinate_matrix())
    # print(matrix_s)
    matrix_p = np.array(random_transposition_matrix_func())
    matrix_g = G

    un_g = matrix_s.dot(G)  # умножение матриц S * G
    un_g = np.array(refactor_matrix_or_list(un_g))  # заполнение матрицы бинарными числами
    un_g = un_g.dot(matrix_p)  # умножение матриц (S * G) * Р
    un_g = np.array(refactor_matrix_or_list(un_g))  # - matrix ^G

    def public_key_func():  # создание списка открытого ключа (^G, t)
        public_key = [to_list(un_g), t]
        return public_key

    def write_public_keys():  # отправка публичного ключа в файл
        public_key_file = open('Public Keys.txt', 'a')
        public_key_file.write(str(public_key_func()))
        public_key_file.close()

    def write_privat_keys(matrix_s, matrix_p, matrix_g):  # отправка приватного ключа в файл
        privat_key_file = open('Privat Keys.txt', 'a')
        privat_key_file.write(str(matrix_s))
        privat_key_file.write(str(matrix_p))
        privat_key_file.write(str(matrix_g))
        privat_key_file.write('-')
        privat_key_file.close()

    write_public_keys()
    write_privat_keys(matrix_s, matrix_p, matrix_g)

    return un_g


def send_message_func(m, un_g):  # здесь происходит кодирование сообщение. c` = m*^G + z
    ciphred_message_text = m.dot(un_g)  # взаимодействует сообщение и ^G
    ciphred_message_text = refactor_matrix_or_list(ciphred_message_text)
    print('Message: ', m, ' or -', to_list(ciphred_message_text))
    received_message_text = ciphred_message_text + random_error_vector()  # добавляется ошибка

    return received_message_text


def write_message(received_message):  # отправка сообщения в файл
    message_file = open('Message.txt', 'a')  # a - дозапись, w - перезапись
    message_file.write(str(received_message))
    message_file.close()


def preparation_encrypt_procedure(m):
    un_g = calculation_un_g()
    received_message = np.array(
        to_list(
            refactor_matrix_or_list(send_message_func(m, un_g))))  # отправка матриц и текста в алгоритм (сам алгоритм)

    write_message(received_message)  # запись по файлам


def create_abstract_text(filename):  # старт программы
    start_time = time.time()

    if filename.lower().endswith('.txt'):  # проверка читаемости текста внутри файла
        file = open(filename, 'rb')
        text = file.read()
        file.close()
        file = open('binary_text.txt', 'w')
        binary_form = "".join(format(i, "08b") for i in text)
        file.write(str(binary_form))
        file.close()
    else:
        file = open(filename, 'rb')
        text = file.read()
        file.close()
        binary_string = ''
        for i in range(len(text)):
            numeric_byte = int(text[i])
            binary = bin(numeric_byte)[2:]
            if len(binary) % 8 == 0:
                binary_string += binary
            else:
                binary = (8 - (len(binary) % 8)) * '0' + binary
                binary_string += binary
        file = open('binary_text.txt', 'w')
        file.write(str(binary_string))
        file.close()
        binary_form = binary_string

    clear_file = open('Message.txt', 'w')  # очистка старых файлов перед записью
    clear_file.close()
    clear_file = open('Public Keys.txt', 'w')
    clear_file.close()
    clear_file = open('Privat Keys.txt', 'w')
    clear_file.close()

    create_code_word()  # запуск кодирования

    time_work = " %s seconds" % (time.time() - start_time)  # вывод
    result = f'Message:\n{binary_form}\nMessage is encrypt and send\nPublic keys are send\nPrivat keys are send\nRunning time: {time_work}'
    print('--------------')

    return result


def create_code_word():  # добавление кодовых слов в бинарный файл
    file_binary = open('binary_text.txt', 'r')
    full_text = file_binary.read()
    file_binary.close()

    while (len(full_text)) % k != 0:
        full_text += '0'
    while len(full_text) != 0:
        word = full_text[0:4]
        one_word = []
        for i in range(len(word)):
            one_word.append(int(word[i]))
        four_bits = np.array(one_word)
        print(four_bits, 'four_bits')
        preparation_encrypt_procedure(four_bits)
        full_text = full_text[4:]
