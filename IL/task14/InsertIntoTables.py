from Connection import Connection
import random  # Add this import statement
import string

class InsertIntoTables(Connection):
    def __init__(self):
        super().__init__()

    def insert_data_from_txt(self, file_path, table_name, columns):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split('|')
                    values = tuple(data[:len(columns)])  # Получаем значения для вставки
                    query = f'''
                        INSERT INTO {table_name} ({', '.join(columns)}) 
                        VALUES ({', '.join(['?'] * len(columns))})
                    '''
                    self.cursor.execute(query, values)
                self.con.commit()
                print(f"Data from {file_path} inserted into {table_name} table successfully")
        except Exception as e:
            print(f"Error inserting data from {file_path} into {table_name} table: {e}")

    def queries(self):
        try:
            # 1. Выбор блюд, содержащих слово 'curry'
            self.cursor.execute("SELECT * FROM Dishes WHERE dish_name LIKE '%Curry%';")
            print("Dishes with 'Curry':")
            print(self.cursor.fetchall())

            # 2. Обновление описания первого блюда
            self.cursor.execute("UPDATE Dishes SET description = 'New description' WHERE id = 1;")
            self.con.commit()
            print("Description updated for Dish ID 1")

            # 3. Удаление блюда с названием 'Sushi Roll'
            self.cursor.execute("DELETE FROM Dishes WHERE dish_name = 'Sushi Roll';")
            self.con.commit()
            print("Deleted 'Sushi Roll' dish")

            # 4. Выбор ингредиентов от поставщика с id = 10
            self.cursor.execute("SELECT * FROM Ingredients WHERE supplier_id = 10;")
            print("Ingredients from Supplier ID 10:")
            print(self.cursor.fetchall())

            # 5. Обновление номера контакта для поставщика с именем 'ABC Foods'
            self.cursor.execute("UPDATE Suppliers SET contact_number = '1234567890' WHERE supplier_name = 'ABC Foods';")
            self.con.commit()
            print("Contact number updated for 'ABC Foods'")

            # 6. Удаление поставщика с email 'info@abcfoods.com'
            self.cursor.execute("DELETE FROM Suppliers WHERE email = 'info@abcfoods.com';")
            self.con.commit()
            print("Deleted supplier with email 'info@abcfoods.com'")

            # 7. Выбор ингредиента с id = 41
            self.cursor.execute("SELECT * FROM Ingredients WHERE id = 41;")
            print("Ingredient with ID 41:")
            print(self.cursor.fetchall())

            # 8. Выбор всех поставщиков с email, содержащим '@example.com'
            self.cursor.execute("SELECT * FROM Suppliers WHERE email LIKE '%@example.com';")
            print("Suppliers with email '@example.com':")
            print(self.cursor.fetchall())

            # 9. Удаление ингредиентов, содержащих слово 'Pasta' в названии
            self.cursor.execute("DELETE FROM Ingredients WHERE ingredient_name LIKE '%Pasta%';")
            self.con.commit()
            print("Deleted ingredients with 'Pasta' in name")

            # 10. Обновление названия ингредиентов для поставщика с id = 11
            self.cursor.execute("UPDATE Ingredients SET ingredient_name = 'aboba' WHERE supplier_id = 11;")
            self.con.commit()
            print("Updated ingredient names for Supplier ID 11")

        except Exception as e:
            print(f"Error executing queries: {e}")
