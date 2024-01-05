def generate_array(n):
    matrix = [[0] * n for _ in range(n)]  # Создаем двумерный массив размером n x n, заполненный нулями

    for i in range(n):
        for j in range(n):
            if i + j == n - 1:  # Проверяем, находится ли элемент на диагонали
                matrix[i][j] = 1
            elif i + j > n - 1:  # Проверяем, находится ли элемент ниже диагонали
                matrix[i][j] = 2

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))  # Выводим элементы строки, разделенные пробелом

n = int(input("Введите размерность матрицы: "))
matrix = generate_array(n)
print_matrix(matrix)
