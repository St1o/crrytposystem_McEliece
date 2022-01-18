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
from numpy import linalg
from Data import *
from Programms_interfaces import refactor_matrix_or_list, to_list, forming_matrix


# принимает матрицу и делает её обратную
def inverse_matrix_func(*args):
    value = args[0]
    inverse_matrix = linalg.inv(value)
    inverse_matrix = refactor_matrix_or_list(inverse_matrix)

    return inverse_matrix


# создаёт транспонированную матрицу H для матрицы G
def transposed_matrix_func(privat_key_g):
    part_i = []
    part_q = []

    for i in range(len(privat_key_g)):
        line_part_i = []
        line_part_q = []
        for j in range(len(privat_key_g[i])):
            x = int(privat_key_g[i][j])
            if j <= (len(privat_key_g) - 1):
                line_part_i.append(x)
            else:
                line_part_q.append(x)
        if type(line_part_i[0]) == int:
            part_i.append(line_part_i)
        else:
            pass
        if type(line_part_q[0]) == int:
            part_q.append(line_part_q)
        else:
            pass

    part_i = np.array(part_i)  # выше получение из матрицы G частей I, Q
    part_q = np.array(part_q)

    q_transpose = part_q.transpose()
    range_j = j + 1
    range_i = j - i

    matrix_h = []
    x = 0
    for i in range(range_i):  # формирование транспонированной матрицы H
        line_matrix_h = []
        y = 0
        for j in range(range_j):
            if j <= (len(q_transpose[0]) - 1):
                line_matrix_h.append(q_transpose[i][j])
            elif j < range_j:
                line_matrix_h.append(part_i[x][y])
                y += 1
        matrix_h.append(line_matrix_h)
        x += 1

    matrix_h = np.array(matrix_h)
    matrix_h = matrix_h.transpose()

    return matrix_h


# создание синдрома
def correction_syndrome(cp, transposed_matrix):
    syndrome = cp.dot(transposed_matrix)

    return syndrome


# исправление сообщения с помощью синдрома
def correction_message_func(syndrome, transposed_matrix, cp):
    error_position = int  # очень важная, но непонятная строчка кода, которая ломает мне мозг
    for i in range(len(transposed_matrix)):
        if str(syndrome) == str(transposed_matrix[i]):
            error_position = i  # показывает позицию где была совершена ошибка
    correction_message = []
    i = 0
    while i < n:
        x = cp[i]
        if i == error_position:  # исправляет ошибку
            if cp[error_position] == 1:
                x = 0
            elif cp[error_position] == 0:
                x = 1
        correction_message.append(x)
        i += 1
    correction_message = np.array(correction_message)  # исправленное сообщение, без ошибки

    return correction_message


# последний этап декодирования
def decrypted(correction_message, inverse_random_non_degenerate_matrix):
    new_cp = []
    for i in range(k):
        new_cp.append(correction_message[i])
    new_cp = np.array(new_cp)
    new_cp = np.array(to_list(refactor_matrix_or_list(new_cp.dot(inverse_random_non_degenerate_matrix))))  # m*S^-1

    return new_cp


# чтение битового сообщения из файла
def read_message():  # я думал, это невозможно. потому что когда видел новый байтовый вывод, то офигевал. я не знал, что такое вывод может быть
    message_file = open('Message.txt', 'rb')
    byte_text = message_file.read()
    message_file.close()
    number_text = int.from_bytes(byte_text, byteorder="big")
    number_text = bin(number_text)
    number_text = str(number_text)[2:]
    number_of_bytes = len(byte_text)
    if len(number_text) % (8 * number_of_bytes) != 0:
        number_text = ((8 * number_of_bytes) - (len(number_text) % (8 * number_of_bytes))) * '0' + number_text
    print(len(number_text), number_text)
    new_int_text = ''
    for i in range(len(number_text)):
        if i != 0:
            if (i + 1) % 8 != 0:
                new_int_text = new_int_text + number_text[i]
        else:
            new_int_text = new_int_text + number_text[i]
    int_text = []
    k = 0
    range_i = int(len(new_int_text) / 7)
    for i in range(range_i):
        row = []
        for j in range(n):
            row.append(int(new_int_text[k]))
            k += 1
        int_text.append(row)
    print(int_text)

    if len(int_text) == 1:
        print('Message is not receive')
    else:
        print('Message is receive')

    return int_text


# чтение битового приватного ключа из файла
def read_privat_keys():
    privat_key_file = open('Privat Keys.txt', 'r')
    string_text = privat_key_file.read()#.split('-')

    if len(string_text) == 1:
        print('Privat keys are not receive')
    else:
        print('Privat keys are receive')
        privat_key_file.close()

        return string_text


# фильтрует символы и добавляет цифры
def take_matrix(privat_key):
    int_symbol = []
    for i in range(len(privat_key)):
        if privat_key[i] == '0':
            int_symbol.append(int(privat_key[i]))
        elif privat_key[i] == '1':
            int_symbol.append(int(privat_key[i]))
    return int_symbol


# алгоритм декодирования по Wiki через синдром
def decrypt_algorithm(message_word, privat_key_s, privat_key_p, privat_key_g):
    random_transposition_matrix = privat_key_p
    random_non_degenerate_matrix = privat_key_s
    inverse_random_transposition_matrix = inverse_matrix_func(random_transposition_matrix)
    inverse_random_non_degenerate_matrix = inverse_matrix_func(random_non_degenerate_matrix)
    cp = message_word.dot(inverse_random_transposition_matrix)
    transposed_matrix = transposed_matrix_func(privat_key_g)
    syndrome = np.array(to_list(refactor_matrix_or_list(correction_syndrome(cp, transposed_matrix))))
    correction_message = correction_message_func(syndrome, transposed_matrix, cp)
    real_word = decrypted(correction_message, inverse_random_non_degenerate_matrix)

    return real_word


# подготовка к процедуре декодирования
def preparation_decrypt_procedure():
    start_time = time.time()
    encoding = 'utf-8'
    errors = 'surrogatepass'

    # распаковка файлов
    message_text = read_message()
    privat_key_text = read_privat_keys()

    i = 0
    real_text_np = []
    while i in range(len(message_text)):
        message_word = np.array(message_text[0])
        privat_key = privat_key_text
        privat_key = privat_key.split('][')
        for j in range(3):
            privat_key_word = take_matrix(privat_key[j])
            if j == 0:
                privat_key_s = forming_matrix(k, k, privat_key_word)
            elif j == 1:
                privat_key_p = forming_matrix(n, n, privat_key_word)
            elif j == 2:
                privat_key_g = forming_matrix(n, k, privat_key_word)
        real_word = decrypt_algorithm(message_word, privat_key_s, privat_key_p,
                                      privat_key_g)  # передаёт сообщение и 3 матрицы
        real_text_np.append(real_word)
        message_text = np.delete(message_text, 0, axis=0)

    # формирование общей картины текста
    real_text_array = str(to_list(refactor_matrix_or_list(real_text_np)))
    real_text = ''
    for i in range(len(real_text_array)):
        if real_text_array[i] == '1':
            real_text += str((real_text_array[i]))
        elif real_text_array[i] == '0':
            real_text += str((real_text_array[i]))
    print('Message is decode.')
    print('Message before decoding: ', real_text)

    # перевод из нулей в слова
    try:
        o = int(real_text, 2)
        ended_text = o.to_bytes((o.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
        opinion = 'Message after decoding:\n'
    except:
        i = 0
        ended_text = ''
        while i < len(real_text):
            ended_text += real_text[i:(i + 8)]
            i += 8
        opinion = 'Binary format. Convert data if you want to read. Data:\n'
    time_work = "\nRunning time: %s seconds" % (time.time() - start_time)
    result = opinion + ended_text + time_work
    print(result)
    print('---------------')

    return result

# preparation_decrypt_procedure()
