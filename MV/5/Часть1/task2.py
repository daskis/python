import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
x = np.array([2, 3, 5, 7])
y = np.array([4, -2, 6, -3])

# Разделение отрезков
h = np.array([x[i + 1] - x[i] for i in range(len(x) - 1)])
alpha = np.array([y[i + 1] - y[i] for i in range(len(y) - 1)])

# Решение системы линейных уравнений
l = np.zeros_like(x)
mu = np.zeros_like(x)
z = np.zeros_like(x)
l[1:-1] = h[:-1]
mu[1:-1] = h[1:]
z[1:-1] = 3 * (alpha[1:] - alpha[:-1])

l[0] = 1
mu[-1] = 1

l, mu, z = map(np.array, (l, mu, z))

# Решение системы линейных уравнений методом прогонки
c = np.zeros_like(x)
l, mu, z = map(np.array, (l, mu, z))

m = np.zeros_like(x)
L = np.zeros_like(x)
m[0] = 0
L[0] = 1

for i in range(1, len(x) - 1):
    m[i] = mu[i - 1] / (L[i - 1] - l[i - 1] * m[i - 1])
    L[i] = 1 - l[i - 1] * m[i]

m[-1] = 0

# Вычисление коэффициентов сплайна
A = y[:-1]
B = alpha - h * (m[:-1] + 2 * m[1:]) / 3
C = m[:-1]
D = (m[1:] - m[:-1]) / (3 * h)

# Интерполяция значений сплайна
def cubic_spline(x_value, x, A, B, C, D):
    i = np.searchsorted(x, x_value) - 1
    dx = x_value - x[i]
    return A[i] + B[i] * dx + C[i] * dx**2 + D[i] * dx**3

# Проверка значения сплайна в узловых точках
spline_values = [cubic_spline(xi, x, A, B, C, D) for xi in x]
print("Значения кубического сплайна в узловых точках:", spline_values)

# Построение графика сплайна и узловых точек
plt.plot(x, y, 'bo', label='Узловые точки')
plt.plot(x, spline_values, 'r-', label='Кубический сплайн')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()