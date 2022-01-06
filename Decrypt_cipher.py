# -*- coding: utf-8 -*-

import numpy as np

from data_wiki import *
from numpy import linalg


def inverse_matrix_func(*args):  # P^-1 or S^-1
    args = args[0]
    inverse_matrix = linalg.inv(args)
    inverse_matrix = refactor_matrix_or_list(inverse_matrix)
    return inverse_matrix


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


def transposed_matrix_func(privat_key_g):
    I = []
    Q = []

    for i in range(len(privat_key_g)):
        I_ = []
        Q_ = []
        for j in range(len(privat_key_g[i])):
            x = int(privat_key_g[i][j])
            if j <= (len(privat_key_g) - 1):
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
    # print('syndrome', np.array(to_list(refactor_matrix_or_list(syndrome))))
    return syndrome


def correction_message_func(syndrome, transposed_matrix, cp):
    for i in range(len(transposed_matrix)):
        if str(syndrome) == str(transposed_matrix[i]):
            error_position = i
            # print(f'Ошибка была в {error_position + 1} позиции')
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
    # print('correction_message:', correction_message)
    return correction_message


def decrypted(correction_message, inverse_random_non_degenerate_matrix):
    new_cp = []
    for i in range(k):
        new_cp.append(correction_message[i])
    new_cp = np.array(new_cp)
    new_cp = np.array(to_list(refactor_matrix_or_list(new_cp.dot(inverse_random_non_degenerate_matrix))))  # m*S^-1
    # print('result', new_cp)
    return new_cp


def read_message():
    message_file = open('message.txt', 'r')
    string_text = message_file.read().split('][')
    int_text = []
    for i in range(len(string_text)):
        int_symbol = []
        for j in range(len(string_text[i])):
            if string_text[i][j] == '0':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] == '1':
                int_symbol.append(int(string_text[i][j]))
        int_text.append(int_symbol)
    print('Message is encrypt and receive')
    return int_text


def read_public_keys():
    public_key_file = open('open keys.txt', 'r')
    string_text = public_key_file.read().split('][')  # !!! УТОЧНИТЬ
    int_text = []
    for i in range(len(string_text)):
        int_symbol = []
        for j in range(len(string_text[i])):
            if string_text[i][j] == '0':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] == '1':
                int_symbol.append(int(string_text[i][j]))
            elif string_text[i][j] != ']':
                t_variable = string_text[i][j + 1]
        int_symbol.pop()
        int_text.append(int_symbol)
    print('Public keys are receive')
    return int_text  # ещё вернуть t
    # print(receive_public_key, t_variable)


def read_privat_keys():
    privat_key_file = open('close keys.txt', 'r')
    string_text = privat_key_file.read().split('-')
    string_text.pop()
    privat_key_file.close()
    print('Privat keys are receive')
    return string_text


def forming_n_k_matrix(public_key_text):
    column = []
    l = 0
    for i in range(k):
        string = []
        for j in range(n):
            string.append(public_key_text[l])
            l += 1
        column.append(string)
    receive_public_key = np.array(column)
    # print(receive_public_key, 'receive_public_key')
    return receive_public_key


def take_matrix(privat_key):
    int_symbol = []
    for i in range(len(privat_key)):
        if privat_key[i] == '0':
            int_symbol.append(int(privat_key[i]))
        elif privat_key[i] == '1':
            int_symbol.append(int(privat_key[i]))
    return int_symbol


def forming_matrix(*args):
    column = []
    l = 0
    for i in range(args[1]):
        string = []
        for j in range(args[0]):
            string.append(args[2][l])
            l += 1
        column.append(string)
    receive_public_key = np.array(column)
    # print(receive_public_key, 'receive key')
    return receive_public_key


def decrypt_algorithm(message_word, privat_key_s, privat_key_p,
                      privat_key_g):  # принимает 4 аргумента - сообщение и 3 матрицы
    random_transposition_matrix = privat_key_p  # 1 матрица
    random_non_degenerate_matrix = privat_key_s  # 2 матрица
    inverse_random_transposition_matrix = inverse_matrix_func(random_transposition_matrix)  # делает обратную
    inverse_random_non_degenerate_matrix = inverse_matrix_func(random_non_degenerate_matrix)  # делает обратную
    cp = c_plus_pi(message_word, inverse_random_transposition_matrix)
    transposed_matrix = transposed_matrix_func(privat_key_g)  # !!!!!
    syndrome = np.array(to_list(refactor_matrix_or_list(correction_syndrome(cp, transposed_matrix))))
    correction_message = correction_message_func(syndrome, transposed_matrix, cp)
    # print('m^G + z = ', received_message, '- b_ciphred_message_text', '\ncp: ',
    #       cp)  # , '\nsyndrome: ',syndrome)#, '\ntransposed_matrix: \n', transposed_matrix)
    real_word = decrypted(correction_message, inverse_random_non_degenerate_matrix)
    return real_word


def preparation_decrypt_procedure(encoding='utf-8', errors='surrogatepass'):
    # распаковка файлов
    message_text = read_message()
    # print(len(message_text))
    public_key_text = read_public_keys()
    privat_key_text = read_privat_keys()
    i = 0
    real_text_np = []
    while i in range(len(message_text)):
        message_word = np.array(message_text[0])
        public_key = forming_n_k_matrix(public_key_text[0])
        # print(message_word, 'message_word')  # , public_key, 'public_key')
        privat_key = privat_key_text[0]
        privat_key = privat_key.split('][')
        for j in range(3):
            privat_key_word = take_matrix(privat_key[j])
            if j == 0:
                privat_key_s = forming_matrix(k, k, privat_key_word)
            elif j == 1:
                privat_key_p = forming_matrix(n, n, privat_key_word)
            elif j == 2:
                privat_key_g = forming_matrix(n, k, privat_key_word)
        real_word = decrypt_algorithm(message_word, privat_key_s, privat_key_p, privat_key_g)  # передаёт сообщение и 3 матрицы
        real_text_np.append(real_word)
        message_text = np.delete(message_text, 0, axis=0)
        privat_key_text = np.delete(privat_key_text, 0, axis=0)
    real_text_array = str(to_list(refactor_matrix_or_list(real_text_np)))
    real_text = ''
    for i in range(len(real_text_array)):
        if real_text_array[i] == '1':
            real_text += str((real_text_array[i]))
        elif real_text_array[i] == '0':
            real_text += str((real_text_array[i]))

    # if (7 - (len(real_text) % 7)) != 0:
    #     x = 7 - (len(real_text) % 7)
    #     real_text = real_text[:-x]
    print('before', real_text)
    o = int(real_text, 2)
    x = o.to_bytes((o.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    # real_text = ''.join(map(lambda x: chr(int(x, 2)), real_text))
    # real_text = o.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    print('after', x)

    # формирование общей картины текста

    # перевод из нулей в слова


preparation_decrypt_procedure()
