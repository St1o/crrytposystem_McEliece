from Data import *
from Programms_interfaces import refactor_matrix_or_list, to_list


def answer():  # создание матрицы ^G = S*G*P
    matrix_s = np.array(checking_null_determinate_matrix())
    matrix_p = np.array(random_transposition_matrix_func())
    matrix_g = G

    un_g = matrix_s.dot(G)  # умножение матриц S * G
    un_g = np.array(refactor_matrix_or_list(un_g))  # заполнение матрицы бинарными числами
    un_g = un_g.dot(matrix_p)  # умножение матриц (S * G) * Р
    un_g = np.array(refactor_matrix_or_list(un_g))  # - matrix ^G

    def public_key_func():  # создание списка открытого ключа (^G, t)
        public_key = [to_list(un_g), t]
        return public_key

    def to_matrix(*args):  # превращает строку в матрицу
        string_text = str(args[0])
        int_text = []
        for i in range(len(string_text)):
            int_symbol = []
            for j in range(len(string_text[i])):
                if string_text[i][j] == '0':
                    int_symbol.append(int(string_text[i][j]))
                elif string_text[i][j] == '1':
                    int_symbol.append(int(string_text[i][j]))
                elif string_text[i][j] != ']':
                    pass
            if len(int_symbol) != 0:
                int_text.append(int_symbol)
        column = []
        l = 0
        for i in range(k):
            row = []
            for j in range(n):
                row.append(int(int_text[l][0]))
                l += 1
            column.append(row)
        int_text = np.array(column)

        return int_text

    def to_byte_string(*args):
        filename = args[1]
        args = args[0]                           # превращает
        line_of_bits = ''                        # в
        for i in range(len(args)):               # строку
            for j in range(len(args[i])):        #
                line_of_bits += str(args[i][j])  #
        file = open(filename, 'ab')
        new_line_of_bits = ''
        i = 0
        if len(line_of_bits) % 8 != 0:
            while i < len(line_of_bits):
                new_line_of_bits += line_of_bits[i:(i + 7)]
                new_line_of_bits += '0'
                i += 7
        i = 0
        while i < len(new_line_of_bits):
            forming_one_byte = new_line_of_bits[i:(i + 8)]
            i += 8
            one_byte = int(int(forming_one_byte, 2))
            one_byte = one_byte.to_bytes(1, byteorder='big')
            file.write(one_byte)
        file.close()

    def write_public_keys():  # отправка публичного ключа в файл
        file = open('Public Keys.txt', 'wb')
        file.close()
        public_key = to_matrix(public_key_func()[0])
        filename = 'Public Keys.txt'
        to_byte_string(public_key, filename)

    def write_privat_keys(matrix_s, matrix_p, matrix_g):  # отправка приватного ключа в файл
        privat_key_file = open('Privat Keys.txt', 'a')
        privat_key_file.write(str(matrix_s))
        privat_key_file.write(str(matrix_p))
        privat_key_file.write(str(matrix_g))

    write_public_keys()
    write_privat_keys(matrix_s, matrix_p, matrix_g)

    return un_g, matrix_s, matrix_p, matrix_g

# answer()
