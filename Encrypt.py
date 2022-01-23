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
from Handshake import answer
from Programms_interfaces import refactor_matrix_or_list, to_list, forming_matrix


def question():
    do_u_wanna_communicate = answer()
    print('The connection with the recipient is established')


def read_public_keys():
    message_file = open('Public Keys.txt', 'rb')
    byte_text = message_file.read()
    message_file.close()
    number_text = int.from_bytes(byte_text, byteorder="big")
    number_text = bin(number_text)
    number_text = str(number_text)[2:]
    number_of_bytes = len(byte_text)
    if len(number_text) % (8 * number_of_bytes) != 0:
        number_text = ((8 * number_of_bytes) - (len(number_text) % (8 * number_of_bytes))) * '0' + number_text
    new_int_text = ''
    for i in range(len(number_text)):
        if i != 0:
            if (i + 1) % 8 != 0:
                new_int_text = new_int_text + number_text[i]
        else:
            new_int_text = new_int_text + number_text[i]
    int_text = []
    l = 0
    for i in range(k * n):
        int_text.append(int(new_int_text[l]))
        l += 1
    int_text = np.array(int_text)
    return int_text


def send_message_func(m, un_g):  # здесь происходит кодирование сообщение. c` = m*^G + z
    ciphred_message_text = m.dot(un_g)  # взаимодействует сообщение и ^G
    ciphred_message_text = refactor_matrix_or_list(ciphred_message_text)
    print('Message: ', m, ' or -', to_list(ciphred_message_text))
    received_message_text = ciphred_message_text + random_error_vector()  # добавляется ошибка

    return received_message_text


def write_message(received_message):  # отправка сообщения в файл
    bit_line = ''
    for i in range(len(received_message)):
        bit_line += str(received_message[i])
    bit_line += '0'
    byte_received_message = int(int(bit_line, 2))
    byte_received_message = byte_received_message.to_bytes(1, byteorder='big')
    message_file = open('Message.txt', 'ab')  # a - дозапись, w - перезапись
    message_file.write(byte_received_message)
    message_file.close()


def preparation_encrypt_procedure(m):
    un_g = read_public_keys()
    un_g = forming_matrix(n, k, un_g)
    received_message = np.array(
        to_list(
            refactor_matrix_or_list(send_message_func(m, un_g))))  # отправка матриц и текста в алгоритм (сам алгоритм)

    write_message(received_message)  # запись по файлам


def create_abstract_text(filename):  # старт программы
    start_time = time.time()

    # filenames = ['Message.txt', 'Public Keys.txt', 'Privat Keys.txt']  # очистка старых файлов перед записью
    # for i in range(len(filenames)):
    #     clear_file = open(filenames[i], 'w')
    #     clear_file.close()

    # question()  # псевдо установка соединения

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

    create_code_word()  # запуск кодирования

    time_work = " %s seconds" % (time.time() - start_time)  # вывод
    result = f'Message is encrypt and send\nPublic keys are send\nPrivat keys are send\nRunning time: {time_work}'
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


# create_abstract_text('1.txt')
