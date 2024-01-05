import math

def compute_sum(target_error):
    row1 = 0
    i = 1
    count = 1
    while True:
        term = 1 / (i ** 2 + 1)
        if term < target_error:
            print(f"Член ряда = {term}, его номер = {i}")
            print(f"Для обычного ряда: сумма всех предыдущих членов ряда = {row1}")
            break
        row1 += term
        i += 1


    row2 = 0
    i = 1
    while True:
        term = 1 / (i ** 4 * (i ** 2 + 1))
        if term < target_error:
            row2 = (math.pi ** 2 / 6) - (math.pi ** 4 / 90) + row2
            print(f"Для ряда с преобразованием: сумма всех предыдущих членов ряда = {row2}")
            break
        row2 += term
        i += 1

    print(f"Разница в вычислениях составляет {row2 - row1}")

target_error = 1e-10
compute_sum(target_error)
