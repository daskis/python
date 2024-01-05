import math
import numpy as np


def calculate_residuals(A, b, x):
    # Невязка r = Ax-b
    r = np.dot(A, x) - b
    return r


def gaus(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        max_elem_in_row = A[i][i]
        if max_elem_in_row == 0:
            raise Exception("Деление на ноль недопустимо")
        for j in range(i + 1, n):
            ratio = A[j][i] / max_elem_in_row
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

#1
print("Система 1")
A = np.array([[10**-4, 1], [1, 2]], dtype=float)
b = np.array([1, 4], dtype=float)

x = gaus(A, b)
r = calculate_residuals(A, b, x)

print("Решение системы X: ", x)
print("Невязки r: ", r)

#2
print("Система 2")
A = np.array([[2.34, -4.21, -11.61], [8.04, 5.22, 0.27], [3.92, -7.99, 8.37]], dtype=float)
b = np.array([14.41, -6.44, 55.56], dtype=float)

x = gaus(A, b)
r = calculate_residuals(A, b, x)

print("Решение системы X: ", x)
print("Невязки r: ", r)

#3
print("Система 3")
A = np.array([
    [4.43, -7.21, 8.05, 1.23, -2.56],
    [-1.29, 6.47, 2.96, 3.22, 6.12],
    [6.12, 8.31, 9.41, 1.78, -2.88],
    [-2.57, 6.93, -3.74, 7.41, 5.55],
    [1.46, 3.62, 7.83, 6.25, -2.35]], dtype=float)
b = np.array([2.62, -3.97, -9.12, 8.11, 7.23], dtype=float)

x = gaus(A, b)
r = calculate_residuals(A, b, x)

print("Решение системы X: ", x)
print("Невязки r: ", r)



