class AllProducts:
    def __init__(self, id, name, price, description, vat, inventory, admin_id):
        self.id = id
        self.name = name
        self.price = float(price)
        self.description = description
        self.vat = float(vat)
        self.inventory = inventory
        self.admin_id = admin_id

    @staticmethod
    def add_new_product(name, price, description, vat, inventory, admin_id):
        run_new = True
        print("Please enter new product")
        while run_new:
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product's price:"))
            product_description = input("Enter product's description:")
            product_vat = float(input("Enter product's vat"))
            product_inventory = int(input("Enter product's inventory:"))
            product_admin_id = input("Enter admin_id")
            answer = input("Do you want to add another product? (y/n)")
            if answer == "y":
                'db_E-handel'.add_new_product(name=product_name, price=product_price,
                                              description=product_description, vat=product_vat, inventory=product_inventory, admin_id=product_admin_id)
            elif answer == "n":
                print("Exit")
                run_new = False
        breakpoint()
