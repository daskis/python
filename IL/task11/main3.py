def count_votes(records):
    votes = {}  # Словарь для подсчета голосов

    for record in records:
        candidate, votes_count = record.split()  # Разделяем запись на фамилию кандидата и число голосов
        votes_count = int(votes_count)  # Преобразуем число голосов в целое

        if candidate in votes:
            votes[candidate] += votes_count  # Если кандидат уже есть в словаре, увеличиваем число голосов
        else:
            votes[candidate] = votes_count  # Иначе, добавляем кандидата в словарь соответствующим числом голосов

    return votes

def print_results(votes):
    sorted_candidates = sorted(votes.keys())  # Сортируем фамилии кандидатов в алфавитном порядке

    for candidate in sorted_candidates:
        print(candidate, votes[candidate])  # Выводим фамилию кандидата и число голосов


num_records = int(input("Введите количество записей: "))
records = []

for _ in range(num_records):
    record = input("Введите запись в формате 'фамилия голоса': ")
    records.append(record)

votes = count_votes(records)
print_results(votes)
