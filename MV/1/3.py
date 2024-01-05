import time
import math


# Функция для вычисления суммы рядов
def compute_sum(x, target_error):
    total_sum = 0
    j = 1

    while True:
        term = (math.sqrt(j ** 3 - x) - math.sqrt(j ** 3 + x)) / (math.sqrt(j ** 3 - x) * math.sqrt(j ** 3 + x))

        if abs(term) < target_error:
            total_sum += term
            print(f"Для x = {x}, член {j}: сумма всех предыдущих членов ряда = {total_sum}")
            break

        total_sum += term
        j += 1

    return total_sum



# Пункт А: Проверка сходимости рядов
# def check_convergence(x):
#     for val in x:
#         # Проверяем сходимость первого ряда: сумма (1 / sqrt(k^3 + x))
#         k = 1
#         while True:
#             term = 1 / math.sqrt(k ** 3 + val)
#             if term < 1e-10:  # Условие сходимости, можно изменить по необходимости
#                 print(f"Первый ряд для x = {val} сходится")
#                 break
#             k += 1
#
#         # Проверяем сходимость второго ряда: сумма (1 / sqrt(k^3 - x))
#         k = 1
#         while True:
#             term = 1 / math.sqrt(k ** 3 - val)
#             if term < 1e-10:  # Условие сходимости, можно изменить по необходимости
#                 print(f"Второй ряд для x = {val} сходится")
#                 break
#             k += 1
#
#
# # Пункт Б: Оценка количества членов ряда для заданной ошибки
# def estimate_terms(x, target_error):
#     for val in x:
#         n_1 = 1
#         while True:
#             term_1 = 1 / ((n_1 + 1) ** (3 / 2))
#             if term_1 < target_error:
#                 break
#             n_1 += 1
#
#         n_2 = 1
#         while True:
#             term_2 = 1 / ((n_2 + 1) ** (3 / 2))
#             if term_2 < target_error:
#                 break
#             n_2 += 1
#
#         max_n = max(n_1, n_2)
#         print(f"Для x = {val}, необходимо примерно {max_n} членов ряда для достижения ошибки меньше {target_error}")
#
#         # Пункт В: Оценка времени для вычисления числа членов ряда
#         time_per_term = 500 * 10 ** -6  # 500 микросекунд на одно слагаемое
#         estimated_time = max_n * time_per_term
#         print(f"Оценка времени для x = {val} и количества членов {max_n}: {estimated_time:.6f} секунд")
#
#
# # Пункт Г: Вычисление s(x) для заданных значений x
x_values = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# k = 10000  # Выберите подходящее значение для k
#
# for x in x_values:
#     start = time.perf_counter()
#     result = compute_sum(x, k)
#     finish = time.perf_counter()
#     print(f"Для x = {x} и количества операций k = {k}, результат: {result}")
#     print(f"Время подсчета для x = {x} и k = {k}: {finish - start:.6f} секунд\n")
#
#     # Пункт А: Проверка сходимости рядов
#     check_convergence([x])
#
#     # Пункт Б: Оценка количества членов ряда, определённого в пункте Б
#     estimate_terms([x], 3e-8)

# Пункт Д: Расчет s(x) для конкретных значений x
specific_x = [0.5, 0.999999999]
target_error = 3e-8  # Ошибка, которую мы хотим достичь
for x_val in x_values:
    result = compute_sum(x_val, target_error)
    print(f"Для x = {x_val}, результат s(x) = {result}")