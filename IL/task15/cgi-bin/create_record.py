#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Создание новой записи</title>
</head>
<body>""")

table = form.getfirst("table")

if table:
    conn = sqlite3.connect('db14.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f"PRAGMA table_info({table})")
        columns = [col[1] for col in cursor.fetchall() if col[1] != 'id']

        print(f"<h1>Создание новой записи в таблице '{table}'</h1>")
        print(f"<form action='/cgi-bin/create_record.py' method='post'>")
        print(f"<input type='hidden' name='table' value='{table}'>")

        for col in columns:
            print(f"<label for='{col}'>{col}:</label>")
            print(f"<input type='text' id='{col}' name='{col}'><br>")

        print("<input type='submit' value='Добавить запись'>")
        print("</form>")

        if form.getvalue(columns[0]):  # Проверка наличия данных в первом поле (можно выбрать любое)
            columns_str = ', '.join(columns)
            values = ', '.join([f"'{form.getvalue(col)}'" for col in columns])
            insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({values});"
            cursor.execute(insert_query)
            conn.commit()
            print("<p>Запись успешно добавлена.</p>")

    except Exception as e:
        print(f"<p>Ошибка: {e}</p>")

    finally:
        conn.close()
else:
    print("<p>Необходимо указать таблицу для добавления записи.</p>")

print("""</body>
</html>""")
