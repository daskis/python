#!/usr/bin/env python3
import cgi
import sqlite3

translated_table_names = {
    "Products": "Продукты",
    "Dishes": "Блюда",
    "Menu": "Меню",
    "Orders": "Заказы",
    "Employees": "Сотрудники",
    "Customers": "Клиенты",
    "Tables": "Столы",
    "Reservations": "Бронирования",
    "Ingredients": "Ингредиенты",
    "Suppliers": "Поставщики"
}

form = cgi.FieldStorage()
table = form.getfirst("table")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Выбор таблицы и просмотр записей</title>
</head>
<body>""")
print("<h1>Выбор таблицы и просмотр записей</h1>")
print("""<form action="/cgi-bin/view_table.py" method="post">
        <label for="table">Выберите таблицу:</label>
        <select name="table" id="table">""")

for name, translation in translated_table_names.items():
    print(f"<option value='{name}'>{translation}</option>")

print("""</select>
        <input type="submit" value="Показать данные">
    </form>""")

conn = sqlite3.connect('db14.db')
cursor = conn.cursor()

try:
    if table:
        cursor.execute(f"SELECT * FROM {table};")
        rows = cursor.fetchall()
        print(f"<h2>Данные из таблицы '{translated_table_names.get(table)}':</h2>")
        print("<table border='1'>")
        print("<tr>")
        for col_name in cursor.description:
            print(f"<th>{col_name[0]}</th>")
        print("<th>Действие</th>")
        print("</tr>")
        for row in rows:
            print("<tr>")
            for col in row:
                print(f"<td>{col}</td>")
            # Добавляем кнопки "Изменить" и "Удалить" для каждой строки таблицы
            print(f"<td><a href='edit_record.py?table={table}&id={row[0]}'>Изменить</a></td>")
            print(f"<td><a href='delete_record.py?table={table}&id={row[0]}'>Удалить</a></td>")
            print("</tr>")
        print("</table>")

        # Добавляем кнопку для добавления записи
        print(f"<a href='create_record.py?table={table}'>Добавить запись</a>")

except Exception as e:
    print(f"<p>Ошибка: {e}</p>")

finally:
    conn.close()

print("""</body>
</html>""")
