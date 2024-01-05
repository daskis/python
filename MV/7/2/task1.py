import numpy as np
from math import erf
import time


def diff_eq(y, x):
    return 2.0 / np.sqrt(np.pi) * np.exp(-x**2)


def euler_method(h, x_values):
    y_values = [0.0]  # начальное значение y(0)

    for x in x_values[:-1]:
        y_next = y_values[-1] + h * diff_eq(y_values[-1], x)
        y_values.append(y_next)

    return np.array(y_values)

# Значения x для таблицы
x_values = np.arange(0.0, 2.1, 0.1)

start_time_euler = time.time()
erf_euler_values = euler_method(0.1, x_values)
end_time_euler = time.time()

erf_eiler_values = [erf(x) for x in x_values]

# Вывод результатов
print("x\t\t\t\t\t erf(x) (Эйлер)\t\t\t erf(x) (Таблица)")
print("-" * 80)
for x, y_euler, y_integral in zip(x_values, erf_euler_values, erf_eiler_values):
    print(f"{x:.1f}\t\t\t\t\t{y_euler:.6f}\t\t\t\t{y_integral:.6f}")

