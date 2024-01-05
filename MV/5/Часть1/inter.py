import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x ** 2)


def cubic_spline(x, y):
    n = len(x)
    h = np.array([x[i + 1] - x[i] for i in range(len(x) - 1)])
    dy = np.array([y[i + 1] - y[i] for i in range(len(y) - 1)])

    alpha = np.zeros(n) # Массив нулей размера n
    alpha[1:-1] = (3.0 / h[1:]) * (dy[1:] / h[1:] - dy[:-1] / h[:-1])

    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)

    # Граничные условия
    l[0] = 1.0
    mu[0] = 0.0
    z[0] = 0.0


    for i in range(1, n - 1):
        l[i] = 2.0 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[-1] = 1.0
    z[-1] = 0.0
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)


    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2.0 * c[j]) / 3.0
        d[j] = (c[j + 1] - c[j]) / (3.0 * h[j])

    #Возвращаем коэф сплайна
    return b, c, d


def plot_function_spline_and_error(n):
    x = np.linspace(-1, 1, n) # создаём массив чисел равномерно зполенный n элементами между -1 и 1
    y = f(x)

    b, c, d = cubic_spline(x, y)

    x_plot = np.linspace(-1, 1, 1000)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x_plot, f(x_plot), label='f(x)', color='blue')

    for i in range(n - 1):

        x_interp = np.linspace(x[i], x[i + 1], 100)
        y_interp = y[i] + b[i] * (x_interp - x[i]) + c[i] * (x_interp - x[i]) ** 2 + d[i] * (x_interp - x[i]) ** 3
        if i == 0:
            plt.plot(x_interp, y_interp, label=f'n = {n}', color='red')
        else:
            plt.plot(x_interp, y_interp, color='red')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'График функции f(x) и кубического сплайна для  (n = {n}) узлов')
    plt.legend()

    # Отрисовка графика ошибки
    plt.subplot(1, 2, 2)
    y_spline = np.zeros_like(x_plot)
    for i in range(n - 1):
        mask = (x_plot >= x[i]) & (x_plot <= x[i + 1])
        dx = x_plot[mask] - x[i]
        y_spline[mask] = y[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
    error = np.abs(f(x_plot) - y_spline)
    plt.plot(x_plot, error, label='error', color='green')
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title(f'Error between f(x) and Cubic Spline (n = {n})')
    plt.legend()


    plt.show()

# узлы 10, 100, 1000

plot_function_spline_and_error(10)
plot_function_spline_and_error(50)
plot_function_spline_and_error(100)