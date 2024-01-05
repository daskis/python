import matplotlib.pyplot as plt


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def vector_subtraction(v1, v2):
    return [x - y for x, y in zip(v1, v2)]


def vector_addition(v1, v2):
    return [x + y for x, y in zip(v1, v2)]


def scalar_division(vector, scalar):
    return [x / scalar for x in vector]


def matrix_vector_product(matrix, vector):
    return [dot_product(row, vector) for row in matrix]


def plot_residuals(residuals_jacobi, residuals_zeidel):
    plt.plot(range(len(residuals_jacobi)), residuals_jacobi, label='Якоби')
    plt.plot(range(len(residuals_zeidel)), residuals_zeidel, label='Зейдель')
    plt.xlabel('Итерации')
    plt.ylabel('Невязки')
    plt.title('График невязок для методов Якоби и Зейделя')
    plt.legend()
    plt.grid(True)
    plt.show()


def jacobi_method(A, b, x0, epsilon):
    n = len(A)
    x = [0] * n
    residuals = []
    iteration = 0

    while True:
        x_new = []
        for i in range(n):
            s = b[i] - sum(A[i][j] * x0[j] for j in range(n) if i != j)
            x_new.append(s / A[i][i])

        residual = max(abs(a - b) for a, b in zip(x_new, x0))
        residuals.append(residual)
        iteration += 1

        if residual < epsilon:
            return x_new, residuals, iteration

        x0 = x_new


def zeidel_method(A, b, x0, epsilon):
    n = len(A)
    x = [0] * n
    residuals = []
    iteration = 0

    while True:
        x_new = x0.copy()

        for i in range(n):
            new_val = (b[i] - sum(A[i][j] * x_new[j] for j in range(n) if i != j)) / A[i][i]
            x_new[i] = new_val

        residual = max(abs(a - b) for a, b in zip(x_new, x0))
        residuals.append(residual)
        iteration += 1

        if residual < epsilon:
            return x_new, residuals, iteration

        x0 = x_new


A = [[12.14, 1.32, -0.78, -2.75],
     [-0.89, 16.75, 1.88, -1.55],
     [2.65, -1.27, -15.64, -0.64],
     [2.44, 1.52, 1.93, -11.43]]

b = [14.78, -12.14, -11.65, 4.26]

# Начальное решение системы
x0 = [0, 0, 0, 0]
epsilon = 1e-10

x_sol_jacobi, residuals_jacobi, iterations_jacobi = jacobi_method(A, b, x0, epsilon)
print('Решение используя метод Якоби:', x_sol_jacobi)
print('Точность:', epsilon)
print('Номер элемента при точности:', iterations_jacobi)

x_sol_zeidel, residuals_zeidel, iterations_zeidel = zeidel_method(A, b, x0, epsilon)
print('Решение используя метод Зейделя:', x_sol_zeidel)
print('Точность:', epsilon)
print('Номер элемента при точности:', iterations_zeidel)

plot_residuals(residuals_jacobi, residuals_zeidel)