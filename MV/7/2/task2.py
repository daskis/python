# ебучие сука кролики
import numpy as np
import matplotlib.pyplot as plt


def runge_kutt(f, x0, y0, h, n):

    x_values = [x0 + i * h for i in range(n+1)]
    y_values = np.zeros((n+1, len(y0)))
    y_values[0] = y0

    for i in range(n):
        k1 = h * np.array(f(x_values[i], y_values[i]))
        k2 = h * np.array(f(x_values[i] + h/2, y_values[i] + k1/2))
        k3 = h * np.array(f(x_values[i] + h/2, y_values[i] + k2/2))
        k4 = h * np.array(f(x_values[i] + h, y_values[i] + k3))

        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        y_values[i+1] = y0

    return x_values, y_values.T


def rabbit_fox_system(x, y):
    alpha = 0.01
    drdt = 2 * y[0] - alpha * y[0] * y[1]
    dfdt = -y[1] + alpha * y[0] * y[1]
    return [drdt, dfdt]


# Параметры системы
initial_conditions = [(2, 3), (10, 20), (1000, 1500), (15, 22), (1000, 1000), (1,1000)]

for r0, f0 in initial_conditions:
    x_values, y_values = runge_kutt(rabbit_fox_system, 0, [r0, f0], 0.001, 7000)

    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values[0], label='зайцы', color='orange')
    plt.plot(x_values, y_values[1], label='лисы',  color='gray')
    plt.title(f'Динамика кроликов и лис при a = {0.01} и r0 = {r0}, f0 = {f0}')
    plt.xlabel('Время')
    plt.ylabel('Популяция')
    plt.legend()
    plt.show()