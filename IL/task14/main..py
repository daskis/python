import os

from CreatingTables import CreatingTables
from InsertIntoTables import InsertIntoTables
if __name__ == "__main__":
    create_table_obj = CreatingTables()
    create_table_obj.creating_tables()
    table_inserter = InsertIntoTables()
    table_names = [
        "Products", "Dishes", "Menu", "Orders", "Employees",
        "Customers", "Tables", "Reservations", "Ingredients", "Suppliers"
    ]

    columns = [
        ["id", "product_name", "price"],
        ["id", "dish_name", "price", "description"],
        ["id", "dish_id"],
        ["id", "dish_id", "order_date"],
        ["id", "employee_name", "position", "salary"],
        ["id", "customer_name", "phone_number", "email"],
        ["id", "table_number", "capacity"],
        ["id", "customer_id", "table_id", "reservation_date"],
        ["id", "ingredient_name", "supplier_id"],
        ["id", "supplier_name", "contact_number", "email"]
    ]

    base_path = "tableData"

    for table_name, columns_list in zip(table_names, columns):
        file_path = os.path.join(base_path, f"{table_name}.txt")
        table_inserter.insert_data_from_txt(file_path, table_name, columns_list)

    table_inserter.queries()
