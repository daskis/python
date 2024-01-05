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
n = 20  # Значение n

x_uniform = np.linspace(a, b, n)
x_values = np.linspace(a, b, 1000)

y_function = f(x_values)
y_interpolation = [lagrange_interpolation(x_uniform, f(x_uniform), xi) for xi in x_values]
y_difference = np.abs(y_function - y_interpolation)


plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(x_values, y_function, label='Исходная функция', color='blue')
plt.title('Исходная функция')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.subplot(132)
plt.plot(x_values, y_interpolation, label='Интерполяционный полином', color='green')
plt.title(f'Интерполяционный полином (n={n})')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid()

plt.subplot(133)
plt.plot(x_values, y_difference, label='Разница', color='red')
plt.title(f'Разница (n={n})')
plt.xlabel('x')
plt.ylabel('Отклонение')
plt.grid()

plt.tight_layout()
plt.show()