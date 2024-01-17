import mysql.connector
db = mysql.connector.connect(

    host="localhost", user="root",
    password="mypassword", database="E-handelSystem"
)
cursor = db.cursor(dictionary=True)


def add_new_admin(name, email, password):
    cursor.execute(f"Insert into Admin (name, email, password)"
                   f"VALUES ('{name}','{email}', {password})")
    db.commit()


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
    cursor.execute("create view admin_view as select customer_id from `E-handelSystem`.cart, `E-handelSystem`.customers"
                   " WHERE cart.id= cart_id")
    db.commit()
