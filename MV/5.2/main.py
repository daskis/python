import numpy as np
import matplotlib.pyplot as plt

# Заданные данные
x = np.array([2, 5, 8, 11, 14, 17])
y = np.array([2.1, 1.3, 1.0, 0.9, 0.8, 0.72])

# Вычисление параметров для различных типов функций

# Линейная функция y = ax + b
coefficients_linear = np.polyfit(x, y, 1)
a_linear, b_linear = np.round(coefficients_linear, 2)
poly_linear = np.poly1d(coefficients_linear)

# Степенная функция y = ax^b -> ln(y) = ln(a) + b * ln(x)
log_x = np.log(x)
log_y = np.log(y)
coefficients_power = np.polyfit(log_x, log_y, 1)
b_power = np.round(coefficients_power[0], 2)
a_power = np.round(np.exp(coefficients_power[1]), 2)
power_function = lambda x: a_power * x**b_power

# Показательная функция y = ab^x -> ln(y) = ln(a) + x * ln(b)
coefficients_exponential = np.polyfit(x, np.log(y), 1)
a_exponential = np.round(np.exp(coefficients_exponential[1]), 2)
b_exponential = np.round(np.exp(coefficients_exponential[0]), 2)
exponential_function = lambda x: a_exponential * b_exponential**x

# Квадратичная функция y = ax^2 + bx + c
coefficients_quadratic = np.polyfit(x, y, 2)
a_quadratic, b_quadratic, c_quadratic = np.round(coefficients_quadratic, 2)
poly_quadratic = np.poly1d(coefficients_quadratic)

# Создание графика для всех функций
plt.figure(figsize=(8, 6))

# Рассеянные точки данных
plt.scatter(x, y, label='Экспериментальные данные')

# График линейной функции
plt.plot(x, poly_linear(x), label=f'Линейная: y = {a_linear}x + {b_linear}', linestyle='--')

# График степенной функции
plt.plot(x, power_function(log_x), label=f'Степенная: y = {a_power}x^{b_power}')

# График показательной функции
plt.plot(x, exponential_function(x), label=f'Показательная: y = {a_exponential} * {b_exponential}^x')

# График квадратичной функции
plt.plot(x, poly_quadratic(x), label=f'Квадратичная: y = {a_quadratic}x^2 + {b_quadratic}x + {c_quadratic}', linestyle='-.')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимирующие функции по методу наименьших квадратов')
plt.legend()
plt.grid(True)
plt.show()
