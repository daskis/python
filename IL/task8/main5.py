def reverse_sequence():
    num = int(input("Введите число: "))

    if num != 0:
        reverse_sequence()
        print(num)



reverse_sequence()
