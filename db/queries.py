create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        price INTEGER,
        product_id INTEGER NOT NULL, 
        photo_id TEXT
    )
"""

insert_product = "INSERT INTO products (name_product, price, product_id, photo_id) VALUES (?, ?, ?, ?)"

select_product = """
                        SELECT pr.name_product, pr.price, pr2.category, pr2.description, pr.product_id, pr.photo_id
                        FROM products pr
                        INNER JOIN products_detail pr2 on pr.product_id = pr2.product_id;
"""

create_table_products_detail = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        product_id INTEGER NOT NULL,
        category TEXT
    )
"""

insert_product_detail = 'INSERT INTO products_detail (description, product_id, category) VALUES (?, ?, ?)'

update_product = "UPDATE {table} SET {field} = ? WHERE product_id = ?"


delete_product = "DELETE FROM products WHERE product_id = ?"
delete_product_detail = "DELETE FROM products_detail WHERE product_id = ?"
