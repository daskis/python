#!/usr/bin/env python3
import sys
import cgi
import sqlite3

sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type: text/html;charset=utf-8\n")


def showData(con):
    try:
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM Cars")
        rows = cursorObj.fetchall()

        # Build HTML table rows dynamically
        table_rows = ""
        for row in rows:
            table_rows += f"""
              <tr>
                <th scope="row">{row[0]}</th>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
                <td>
                    <form method="POST" action="DeleteCar.py">
                        <input type="hidden" name="car_id" value="{row[0]}">
                        <button type="submit" class="btn btn-danger">Удалить</button>
                    </form>
                </td>
              </tr>
            """

        pattern = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta
                name="viewport"
                content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
                />
                <meta http-equiv="X-UA-Compatible" content="ie=edge" />
                <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                rel="stylesheet"
                integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                crossorigin="anonymous"
                />
                <link rel="stylesheet" type="text/css" href="../../style.css" />
                <script
                src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
                crossorigin="anonymous"
                ></script>
                <title>Просмотр записей || Cars</title>
            </head>
            <body>
                <header>
                <div class="header-wrapper">
                    <div class="header row">
                    <nav class="navbar navbar-expand-lg container-fluid">
                        <div class="container-fluid">
                        <a class="navbar-brand" href="http://localhost:8000">
                        Администрирование БД "Автобаза"
                        </a>

                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                            <li class="nav-item dropdown">
                                <a
                                class="nav-link dropdown-toggle"
                                href="#"
                                role="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                >
                                Qualification
                                </a>
                                <ul class="dropdown-menu">
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/QualForm/QualFormShow.html"
                                    >Посмотреть записи</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/QualForm/QualFormInsert.html"
                                    >Добавить запись</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/QualForm/QualFormUpdate.html"
                                    >Изменить запись</a
                                    >
                                </li>
                                </ul>
                            </li>
                            <li class="nav-item dropdown">
                                <a
                                class="nav-link dropdown-toggle"
                                href="#"
                                role="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                >
                                Routes
                                </a>
                                <ul class="dropdown-menu">
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/RoutesForm/RoutesFormShow.html"
                                    >Посмотреть записи</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/RoutesForm/RoutesFormInsert.html"
                                    >Добавить запись</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/RoutesForm/RoutesFormUpdate.html"
                                    >Изменить запись</a
                                    >
                                </li>
                                </ul>
                            </li>
                            <li class="nav-item dropdown">
                                <a
                                class="nav-link dropdown-toggle"
                                href="#"
                                role="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                >
                                Cars
                                </a>
                                <ul class="dropdown-menu">
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/CarsForm/CarsFormShow.html"
                                    >Посмотреть записи</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/CarsForm/CarsFormInsert.html"
                                    >Добавить запись</a
                                    >
                                </li>
                                <li>
                                    <a
                                    class="dropdown-item"
                                    href="http://localhost:8000/CarsForm/CarsFormUpdate.html"
                                    >Изменить запись</a
                                    >
                                </li>
                                </ul>
                            </li>
                            </ul>
                        </div>
                        </div>
                    </nav>
                    </div>
                </div>
                </header>
                <main class="container h-100">
                        <div class="d-flex align-items-center justify-content-center h-100">
                            <div class="d-flex flex-column">
                            <h1>Окно вывода данных таблицы</h1>

                             <table class="table table-secondary table-striped table-hover">
                                <thead>
                                <tr>
                                    <th scope="col">Id</th>
                                    <th scope="col">Марка авто</th>
                                    <th scope="col">Цвет авто</th>
                                    <th scope="col">Номер авто</th>
                                    <th scope="col">Действие</th>
                                </tr>
                                </thead>
                                <tbody>
                                {table_rows}
                                </tbody>
                            </table>

                            <div class="alert alert-success" role="alert">
                                    Удаление из базы данных произведено успешно
                                </div>
                            </div>
                        </div>
                        </main>
                <footer class="py-3 my-4">
                <div
                    class="footer-wrapper d-flex justify-content-center align-items-center"
                >
                    <p class="text-center text-muted mb-0 font-size-increased mr-2">
                    © 2023 Emelyanenko A.A.
                    </p>
                    <a href="https://github.com/LumateDev">
                    <img
                        src="../../src/git.svg"
                        alt="icon"
                        class="ml-2"
                        width="24"
                        height="24"
                    />
                    </a>
                </div>
                </footer>
            </body>
            </html>"""
        
        print(pattern)
        con.commit()


    except Exception as e:
        error_message = f'''<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                rel="stylesheet"
                integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                crossorigin="anonymous"
            />
            <link rel="stylesheet" type="text/css" href="../../style.css" />
            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
            crossorigin="anonymous"
            ></script>
            <title>Error page</title>
        </head>
        <body>
            <div class="alert alert-danger" role="alert">Произошла ошибка: {str(e)}</div>
        </body>
        </html>'''
        print(error_message)

# Получение данных из формы
form = cgi.FieldStorage()
car_id = form.getvalue("car_id")

try:
    con = sqlite3.connect("AutoBase.db")
    cursorObj = con.cursor()
    cursorObj.execute(f"DELETE FROM Cars WHERE Id = {car_id}")
    con.commit()
    showData(con)
    con.close()
    

except Exception as e:
    print(f"Произошла ошибка при удалении записи: {str(e)}")
    error_message = f'''<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                rel="stylesheet"
                integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                crossorigin="anonymous"
            />
            <link rel="stylesheet" type="text/css" href="../../style.css" />
            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
            crossorigin="anonymous"
            ></script>
            <title>Error page</title>
        </head>
        <body>
            <div class="alert alert-danger" role="alert">Произошла ошибка удаления: {str(e)}</div>
        </body>
        </html>'''
    print(error_message)





