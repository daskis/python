import math

args = [0.5, 1.0, 5.0, 10.0]


def factorial(num):
    elem = 1

    if elem == 0:
        return 1

    for i in range(2, num + 1):
        elem *= i

    return elem


for elem in args:
    func1 = 2 / math.sqrt(math.pi)
    func2 = 0
    for n in range(0, 100 + 1):
        func2 += (pow(-1, n) * pow(elem, 2 * n + 1)) / (factorial(n) * (2 * n + 1))

    func = func1 * func2
    print("X = " + str(elem) + "," + "func = " + str(func) + "," + "Erf = " + str(math.erf(elem)))
    print("Погрешность " + str(abs(math.erf(elem) - func)))

