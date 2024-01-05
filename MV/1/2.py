import time

n = 100


def factorial(num):
    elem = 1

    if elem == 0:
        return 1

    for i in range(2, num + 1):
        elem *= i

    return elem


def function1(x):
    func1 = 0
    for n1 in range(1, n + 1):
        func1 += 1 / (n1 * (n1 + x))

    return func1


def function2(x):
    func2 = 0
    for n2 in range(1, n + 1):
        func2 += (1 / n2) - (1 / (n2 + 1))
    return func2


def main():

    x = 0.1

    while x <= 1.0:
        tic = time.perf_counter()
        result1 = function1(1)
        toc = time.perf_counter()

        print(f"Вычисление f(1) заняло {toc - tic} секунд")

        tic1 = time.perf_counter()
        result2 = function1(x)
        toc1 = time.perf_counter()
        print(f"Вычисление f(x) заняло {toc1 - tic1} секунд")

        print(
            "F(1)  = " + str(result1) + "," + "f(x) = " + str(result1) + "," "Разность " + str(abs(result1 - result2)))
        x += 0.1


if __name__ == "__main__":
    main()
