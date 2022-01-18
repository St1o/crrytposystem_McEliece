import numpy as np


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

    return receive_public_key
