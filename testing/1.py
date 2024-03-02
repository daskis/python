def checkType(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return "Это равносторонний треугольник"
        elif a == b or b == c or a == c:
            return "Это равнобедренный треугольник"
        else:
            if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
                return "Это прямоугольный треугольник"
            else:
                return "Это разносторонний треугольник"
    else:
        return "Треугольник с такими сторонами невозможен"


a, b, c = map(int, input("Введите 3 стороны треугольника через пробел: ").split())

triangle_type = checkType(a, b, c)
print(triangle_type)
