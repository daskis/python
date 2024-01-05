# Ввод данных
num_kegels, num_throws = map(int, input("Введите количество кеглей и количество бросков: ").split())
throws = []

# Ввод бросков
for _ in range(num_throws):
    throws.append(tuple(map(int, input("Введите номера первой и последней сбитой кегли: ").split())))

# Инициализация списка кеглей
kegels = ["I"] * num_kegels

# Проверка сбитых кеглей
for throw in throws:
    for i in range(throw[0] - 1, throw[1]):
        kegels[i] = "."

# Вывод результата
print("".join(kegels))
