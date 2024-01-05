first_date = int(input("Первая дата \n"))
second_date = int(input("Вторая дата \n"))
most_pop_name = ""
most_pop_count = 0

def return_most_popular_names(file):
    lines = file.readlines()
    m_count = 0
    m_name = ""
    for line in lines:
        name, count = line.split()
        count = int(count)
        if count > m_count:
            m_count = count
            m_name = name

    return m_name, m_count

for i in range(first_date, second_date + 1):
    girlFile = open(f"BabyNames/{i}_GirlsNames.txt", "r")
    boysFile = open(f"BabyNames/{i}_BoysNames.txt", "r")
    girl_name, girl_count = return_most_popular_names(girlFile)
    boy_name, boy_count = return_most_popular_names(boysFile)

    if girl_count > most_pop_count:
        most_pop_count = girl_count
        most_pop_name = girl_name

    if boy_count > most_pop_count:
        most_pop_count = boy_count
        most_pop_name = boy_name

    girlFile.close()
    boysFile.close()

print(f"Самое популярное имя среди всех дат: {most_pop_name}, количество раз: {most_pop_count}")
