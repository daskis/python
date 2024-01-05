import math


def sign_func(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

# e = math.pow(10, 30)
# a *= e
# b *= e
# c *= e

d = math.pow(b, 2) - 4 * a * c
if d > 0:
    x1disc = (-b + math.sqrt(d)) / (2 * a)
    x2disc = (-b - math.sqrt(d)) / (2 * a)

    x1sign = -(b + sign_func(b) * math.sqrt(d)) / (2 * a)
    x2sigh = c / (a * x1sign)

    print("discriminant :" + str(d))
    print("x1 disc: " + str(x1disc))
    print("x2 disc:" + str(x2disc))

    print("x1sign: " + str(x1sign))
    print("x2sign: " + str(x2sigh))

else:
    print("Я не обрабатываю комлпексный случай")
