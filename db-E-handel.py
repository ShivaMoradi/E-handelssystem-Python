import mysql.connector

db = mysql.connector.connect(

    host="localhost", user="root",
    password="mypassword", database="E-handelSystem"
)
cursor = db.cursor(dictionary=True)


def add_new_product(name, price, description, vat, inventory, admin_id):
    cursor.execute(f"INSERT INTO products (name, price, description, vat, inventory, admin_id)"
                   f"VALUES ('{name}', {price}, '{description}', {vat}, {inventory}, {admin_id})")
    db.commit()


def delete_product_by_id():
    cursor.execute("DELETE* FROM products WHERE id = %s")
    db.commit()


def edit_product():
    cursor.execute("UPDATE products SET")
    db.commit()


def view_products():
    cursor.execute("create view customer_cart as select * from cart WHERE customer_id is not null")
    db.commit()



