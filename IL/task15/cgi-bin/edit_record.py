#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Редактирование и обновление записи</title>
</head>
<body>""")

if 'table' in form and 'id' in form:
    table = form.getfirst("table")
    record_id = form.getfirst("id")

    if table and record_id:
        conn = sqlite3.connect('db14.db')  # Название вашей базы данных
        cursor = conn.cursor()

        try:
            if 'update_record' in form:  # Обработка обновления записи
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
            else:  # Отображение формы редактирования
                cursor.execute(f"SELECT * FROM {table} WHERE id={record_id};")
                row = cursor.fetchone()
                if row:
                    print(f"<h1>Редактирование записи в таблице '{table}'</h1>")
                    print(f"<form action='/cgi-bin/update_record.py' method='post'>")
                    print(f"<input type='hidden' name='table' value='{table}'>")
                    print(f"<input type='hidden' name='id' value='{record_id}'>")

                    for i, col_name in enumerate(cursor.description):
                        col = col_name[0]
                        if (col != "id"):
                            print(f"<label for='field{i}'>{col}:</label>")
                            print(f"<input type='text' id='field{i}' name='{col}' value='{row[i]}'>")
                        print("<br>")

                    print("<input type='submit' name='update_record' value='Изменить данные'>")
                    print("</form>")
                else:
                    print("<p>Запись не найдена.</p>")
        except Exception as e:
            print(f"<p>Ошибка: {e}</p>")
        finally:
            conn.close()
    else:
        print("<p>Некорректные данные для редактирования.</p>")
else:
    print("<p>Необходимо указать таблицу и ID записи.</p>")

print("""</body>
</html>""")
