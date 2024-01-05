#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обновление записи</title>
</head>
<body>""")

if 'table' in form and 'id' in form:
    table = form.getfirst("table")
    record_id = form.getfirst("id")

    if table and record_id:
        conn = sqlite3.connect('db14.db')  # Название вашей базы данных
        cursor = conn.cursor()

        try:
            columns = []
            cursor.execute(f"PRAGMA table_info({table})")
            for col in cursor.fetchall():
                columns.append(col[1])

            data = {key: form.getvalue(key) for key in form.keys()}

            update_query = f"UPDATE {table} SET "
            for col in columns:
                if col in data and col != 'id':
                    value = data[col]
                    update_query += f"{col} = '{value}', "

            update_query = update_query.rstrip(', ')
            update_query += f" WHERE id = {record_id};"

            cursor.execute(update_query)
            conn.commit()
            print(f"<h1>Данные в таблице '{table}' успешно обновлены</h1>")
        except Exception as e:
            print(f"<p>Ошибка: {e}</p>")
        finally:
            conn.close()
    else:
        print("<p>Некорректные данные для обновления.</p>")
else:
    print("<p>Необходимо указать таблицу и ID записи.</p>")

print("""</body>
</html>""")
