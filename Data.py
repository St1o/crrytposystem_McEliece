import numpy as np
import random

global k, n, t, G
k = 4
n = 7
t = 1

# пример кода Гоппы
G = np.array([[1, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1]])


# создание вектора нулей с единицей на месте ошибки
def random_error_vector():
    rand = random.randint(0, 6)
    error_vector = []
    for i in range(n):
        if i == rand:
            x = [1]
        else:
            x = [0]
        error_vector.append(x)
    error_vector = np.array(error_vector)

    return error_vector


# создание случайной невырожденной матрицы
def random_non_degenerate_matrix_func():
    matrix_s = []
    for i in range(k):
        b = []
        for j in range(k):
            x = random.randint(0, 1)
            b.append(x)
        matrix_s.append(b)
    matrix_s = np.array(matrix_s)

    return matrix_s


# создание случайной матрицы перестановок. матрица, где в каждой строке и каждом столбце 1 единица
def random_transposition_matrix_func():
    matrix_p = []
    list_n = list(range(n))
    random.shuffle(list_n)

    for i in range(n):
        line_matrix_p = []
        for j in range(n):
            if list_n[j] == i:
                line_matrix_p.append(1)
            else:
                line_matrix_p.append(0)
        matrix_p.append(line_matrix_p)
    matrix_p = np.array(matrix_p)

    return matrix_p


# проверка определителя матрицы. он должен быть +-1
def checking_null_determinate_matrix():
    random_non_degenerate_matrix = random_non_degenerate_matrix_func()
    while np.linalg.det(random_non_degenerate_matrix) != (1.0 or -1.0):
        random_non_degenerate_matrix = random_non_degenerate_matrix_func()
    else:
        return random_non_degenerate_matrix
