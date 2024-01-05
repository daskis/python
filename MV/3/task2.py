def calculate_rank(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rank = 0
    row_index = 0

    for col in range(cols):
        swap_row = row_index

        for row in range(row_index, rows):
            if abs(matrix[row][col]) > abs(matrix[swap_row][col]):
                swap_row = row

        if abs(matrix[swap_row][col]) < 1e-10:  # настраиваемая точность
            continue

        matrix[swap_row], matrix[row_index] = matrix[row_index], matrix[swap_row]

        for row in range(row_index + 1, rows):
            ratio = matrix[row][col] / matrix[row_index][col]
            for i in range(col, cols):
                matrix[row][i] -= ratio * matrix[row_index][i]

        row_index += 1
        rank += 1

    return rank


def gaus(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        if A[i][i] == 0:
            raise Exception("Деление на ноль недопустимо")
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]

    # Обратный ход
    x = [0] * n
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i][j] * x[j]
        x[i] = (b[i] - s) / A[i][i]

    return x


A = [[0.1, 0.2, 0.3],
     [0.4, 0.5, 0.6],
     [0.7, 0.8, 0.9]]
b = [0.1, 0.3, 0.5]

solution = gaus(A, b)
rank = calculate_rank(A)
print(rank)

if rank < len(A[1]):
    print("Система имеет беско множество решений", solution)
else:
    print("Единственное решение" , solution)

"Если ранг матрицы равен числу неизвестных, то решение единственное," \
" если ранг матрицы < n, то решений беск много " \
"P.S. Теорема кронекера- каппелли"