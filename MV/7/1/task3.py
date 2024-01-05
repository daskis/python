import numpy as np


def f_interval_1(x):
    return np.exp(x**2)


def f_interval_2(x):
    return 1 / (4 - np.sin(16 * np.pi * x))


def simpson_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1) # узлы интегрирования
    y = func(x)

    result = h / 3 * (y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n-1, 2)) + y[-1])

    return result

# Интегрирование для интервала [0, 2]
result_interval_1 = simpson_rule(f_interval_1, 0, 2, 1000)

# Интегрирование для интервала (2, 4]
result_interval_2 = simpson_rule(f_interval_2, 2, 4, 1000)

# Суммируем результаты
final_result = result_interval_1 + result_interval_2

print(f"Итоговый результат с использованием метода Симпсона: {final_result:.8f}")

"""Метод Симпсона сходится к решению квадратично, что означает, что увеличение числа узлов в два раза приводит к увеличению точности в четыре раза."""