num = int(input("Введите число последовательности: "))
max_element = num
count = 0

while num != 0:
    if num > max_element:
        max_element = num
        count = 1
    elif num == max_element:
        count += 1
    num = int(input("Введите число последовательности: "))

print("Количество элементов, равных наибольшему элементу:", count)
