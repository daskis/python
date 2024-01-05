import numpy as np
from scipy.interpolate import CubicSpline


def spline_rule(x):
    return 4 / (1 + x ** 2)


def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    return h * result


def rectangular_rule(func, a, b, n):
    h = (b - a) / n
    result = sum(func(a + i * h) for i in range(n))
    return h * result


def pi_approximation_with_spline(n):
    x = np.linspace(0, 1, n + 1)
    y = spline_rule(x)
    cs = CubicSpline(x, y)
    approx_pi = cs.integrate(0, 1)
    return approx_pi


def main_approximations():
    methods = [trapezoidal_rule, rectangular_rule]
    for method in methods:
        for n in [8, 32, 128]:
            approx_pi = method(spline_rule, 0, 1, n)
            print(f"{method.__name__}, n={n} {approx_pi:.8f}")
        print("\n")


def main_spline_approximation():
    for n in [8, 32, 128]:
        approx_pi = pi_approximation_with_spline(n)
        print(f"Spline, n={n}: {approx_pi:.8f}")


def calculate_error(approximation, exact_value):
    return abs(approximation - exact_value)


"""
    Для метода трапеций:
При уменьшении h, ошибка уменьшается. Ошибка приблизительно пропорциональна  h^2, что соответствует методу второго порядка.

    Для сплайн-квадратур:
При уменьшении h, ошибка также уменьшается, но с более высокой скоростью, чем у метода трапеций.
Ошибка не обязательно пропорциональна  h или  h^2— она может уменьшаться с более высокой степенью.
"""


def main():
    exact_pi = np.pi
    print("\n")
    print("n\tМетод трапеций \tМетода прямоугольников \tСплайн квадратуры")
    print("------------------------------------------------------")
    for n in [8, 32, 128]:
        trapezoidal_result = trapezoidal_rule(spline_rule, 0, 1, n)
        rectangular_result = rectangular_rule(spline_rule, 0, 1, n)
        spline_result = pi_approximation_with_spline(n)

        trapezoidal_error = calculate_error(trapezoidal_result, exact_pi)
        rectangular_error = calculate_error(rectangular_result, exact_pi)
        spline_error = calculate_error(spline_result, exact_pi)

        print(f"{n}\t\t{trapezoidal_error:.8f}\t\t{rectangular_error:.8f}\t\t{spline_error:.8f}")


if __name__ == "__main__":
    main_approximations()
    main_spline_approximation()
    main()

