import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
# Наше пространство по которому распределяется тепло
# Задаем параметры задачи
T = 1.0  # Общее время
h = np.pi / 20  # Шаг по пространственной переменной x
tau = 0.0001  # Шаг по временной переменной t
r = tau / h ** 2  # Параметр, определяющий устойчивость схемы - лямба
x = np.arange(0, np.pi / 2 + h, h)  # Массив значений x
t = np.arange(0, T + tau, tau)  # Массив значений t
N = len(x)  # Количество узлов по x
M = len(t)  # Количество узлов по t

# Задаем начальное и граничное условия
u0 = np.sin(x)  # Начальное условие u(x, 0) = sin x первый столбик сетки заполнен
u_left = np.zeros(M)  # Граничное условие u(0, t) = 0 первая строчка сетки 0
u_right = np.exp(-t)  # Граничное условие u(pi/2, t) = e^(-t) последняя строчка сетки - экспонента

# Задаем точное решение для проверки
u_exact = np.exp(-t)[:, np.newaxis] * np.sin(x)  # u(x, t) = e^(-t) * sin x [:, np.newaxis]:
# Эта конструкция изменяет форму массива, полученного после вычисления экспоненты. np.newaxis используется для добавления новой оси,
# так что массив, который изначально, например, был одномерным, превращается в двумерный с одной из размерностей, равной единице (как вектор-столбец).
# Это делается для того, чтобы можно было выполнить операцию по элементам с другим массивом.


# Функция для решения уравнения с использованием явной разностной схемы
def explicit_scheme(N, M, r, u0, u_left, u_right):
    # Создаем массив для хранения значений решения
    u = np.zeros((M, N))
    # Заполняем первую строку начальным условием
    u[0, :] = u0
    # Заполняем первый и последний столбец граничными условиями
    u[:, 0] = u_left
    u[:, -1] = u_right
    # Цикл по временным слоям
    for m in range(M - 1):
        # Цикл по пространственным узлам
        for n in range(1, N - 1):
            # Применяем формулу явной разностной схемы
            u[m + 1, n] = u[m, n] + r * (u[m, n - 1] - 2 * u[m, n] + u[m, n + 1])
    # Возвращаем массив значений решения
    return u


# Функция для решения уравнения с использованием неявной разностной схемы
def implicit_scheme(N, M, r, u0, u_left, u_right):
    # Создаем массив для хранения значений решения
    u = np.zeros((M, N))
    # Заполняем первую строку начальным условием
    u[0, :] = u0
    # Заполняем первый и последний столбец граничными условиями
    u[:, 0] = u_left
    u[:, -1] = u_right
    # Создаем матрицу коэффициентов системы линейных уравнений
    A = np.zeros((N - 2, N - 2))
    # Заполняем главную диагональ
    np.fill_diagonal(A, 1 + 2 * r)
    # Заполняем верхнюю и нижнюю диагонали
    np.fill_diagonal(A[1:, :-1], -r)
    np.fill_diagonal(A[:-1, 1:], -r)
    # Цикл по временным слоям
    for m in range(M - 1):
        # Создаем вектор правой части системы линейных уравнений
        b = u[m, 1:-1]
        # Учитываем граничные условия
        b[0] += r * u[m + 1, 0]
        b[-1] += r * u[m + 1, -1]
        # Решаем систему линейных уравнений
        u[m + 1, 1:-1] = solve(A, b)
    # Возвращаем массив значений решения
    return u


# Функция для вычисления точного решения
def exact_solution(x, t):
    # Возвращаем массив значений точного решения
    return np.exp(-t) * np.sin(x)


# Функция для построения графика решения
def plot_solution(x, t, u, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Преобразуем массивы x и t в двумерные сетки
    X, T = np.meshgrid(x, t)
    # Строим поверхность решения
    ax.plot_surface(X, T, u, cmap='jet')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('u')
    ax.set_title(title)
    plt.show()


def main():
    global u_exact
    u_explicit = explicit_scheme(N, M, r, u0, u_left, u_right)
    print('Явная разностная схема:')
    print('Параметр r =', r)
    print('Устойчивость схемы зависит от значения r')
    print('Схема устойчива, если r <= 0.5')
    print('Схема неустойчива, если r > 0.5')
    if r <= 0.5:
        print('В нашем случае схема устойчива')
    else:
        print('В нашем случае схема неустойчива')
        print('Возможны переполнения или осцилляции')

    # Вывод ответов
    t_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for t_value in t_values:
        m = int(t_value / tau)
        print(f'Значение решения при t = {t_value}:')
        print(u_explicit[m, :])
        print()

    print('Максимальная абсолютная ошибка  явной схемы по сравнению с точным решением:')
    print(np.max(np.abs(u_explicit - u_exact)))



    plot_solution(x, t, u_explicit, 'Явная разностная схема')
    u_implicit = implicit_scheme(N, M, r, u0, u_left, u_right)

    print('Неявная разностная схема:')
    print('Параметр r =', r)
    print('Устойчивость схемы не зависит от значения r')
    print('Схема всегда устойчива')
    print('Значение решения в последний момент времени:')
    print(u_implicit[-1, :])
    print('Максимальная абсолютная ошибка неявной схемы по сравнению с точным решением:')
    print(np.max(np.abs(u_implicit - u_exact)))

    plot_solution(x, t, u_implicit, 'Неявная разностная схема')
    plt.figure(figsize=(10, 8))

    # Задаем список значений t, для которых будем строить графики
    t_list = [0, 0.25, 0.5, 0.75, 1]

    # Цикл по значениям t
    for i, t_value in enumerate(t_list):
        # Находим индекс временного слоя, соответствующего значению t
        m = int(t_value / tau)

        plt.subplot(2, 3, i + 1)
        plt.plot(x, u_exact[m, :], 'ro-', label='Точное решение')
        plt.plot(x, u_explicit[m, :], 'bs-', label='Явная схема')
        plt.plot(x, u_implicit[m, :], 'g^-', label='Неявная схема')

        plt.title(f'Решение при t = {t_value}')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('u')
    plt.show()


main()