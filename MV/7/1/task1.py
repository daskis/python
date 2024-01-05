import math
import time


def calculate_erf(x, n=1000):
    def integrand(t):
        return math.exp(-t ** 2)

    def trapezoidal_rule(a, b, n):
        h = (b - a) / n
        result = 0.5 * (integrand(a) + integrand(b))
        for i in range(1, n):
            result += integrand(a + i * h)
        return h * result

    return (4 / math.pi) * trapezoidal_rule(0, x, n)


def main():
    print("x\t\t erf(x)\t\t Известное значение erf(x)")
    print("-------------------------------------------")

    start_time = time.time()

    for x in [i / 10 for i in range(21)]:
        calculated_result = calculate_erf(x)
        known_result = math.erf(x)
        print(f"{x:.1f}\t\t{calculated_result:.6f}\t\t{known_result:.6f}")

    end_time = time.time()

    print("\nВремя выполнения: {:.6f} сек.".format(end_time - start_time))


if __name__ == "__main__":
    main()