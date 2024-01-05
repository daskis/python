#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Удаление записи</title>
</head>
<body>""")

if 'table' in form and 'id' in form:
    table = form.getfirst("table")
    record_id = form.getfirst("id")

    if table and record_id:
        conn = sqlite3.connect('db14.db')
        cursor = conn.cursor()

        try:
            cursor.execute(f"DELETE FROM {table} WHERE id={record_id};")
            conn.commit()
            print(f"<h1>Запись в таблице '{table}' с ID {record_id} успешно удалена</h1>")
        except Exception as e:
            print(f"<p>Ошибка при удалении записи: {e}</p>")
        finally:
            conn.close()
    else:
        print("<p>Некорректные данные для удаления.</p>")
else:
    print("<p>Необходимо указать таблицу и ID записи.</p>")

print("""</body>
</html>""")
