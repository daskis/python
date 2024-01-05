import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x**2)


# Функция для вычисления интерполяционного полинома Лагранжа
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for j in range(n):
        term = y[j]
        for k in range(n):
            if k != j:
                term *= (xi - x[k]) / (x[j] - x[k])
        result += term
    return result


a, b = -1, 1  # Отрезок [-1, 1]
n_values = [5, 10, 20, 100]  # узлы

#  равномерно узлы
x_uniform = np.linspace(a, b, max(n_values))

# Создайте Чебышевские узлы
def chebyshev_nodes(n):
    return np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))

# Создайте графики для различных значений n
for n in n_values:
    x_chebyshev = (b - a) / 2 * chebyshev_nodes(n) + (a + b) / 2
    y = f(x_uniform)
    y_interpolated_uniform = [lagrange_interpolation(x_uniform, y, xi) for xi in x_uniform]
    y_interpolated_chebyshev = [lagrange_interpolation(x_chebyshev, y, xi) for xi in x_uniform]
    plt.figure(figsize=(10, 5))
    plt.plot(x_uniform, y, label='Исходная функция', linewidth=2)
    plt.plot(x_uniform, y_interpolated_uniform, label=f'Интерполяция (равноотстаящие узлы, n={n})', linestyle='--')
    plt.plot(x_uniform, y_interpolated_chebyshev, label=f'Интерполяция (Чебышевские узлы, n={n})', linestyle='-.')
    plt.legend()
    plt.title(f'Интерполяция для n={n}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()