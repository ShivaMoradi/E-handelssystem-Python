import database

products_info = {'name': '<NAME>', 'price': '<price>', 'description': '<description>', 'vat': '<vat>',
                 'inventory': '<inventory>', 'admin_id': '<admin_id>'}


class AllProducts:
    def __init__(self, name, price, description, vat, inventory, admin_id):
        self.name = name
        self.price = price
        self.description = description
        self.vat = vat
        self.inventory = inventory
        self.admin_id = admin_id

    def add_new_product(self):
        run_new = True
        print("Please enter new product")
        while run_new:
            self.name = input("Enter product name: ")
            self.price = float(input("Enter product's price:"))
            self.description = input("Enter product's description:")
            self.vat = float(input("Enter product's vat"))
            self.inventory = int(input("Enter product's inventory:"))
            self.admin_id = input("Enter admin_id")
            answer = input("Do you want to add another product? (y/n)")
            if answer == "y":
                database.add_new_product(name=self.name, price=self.price, description=self.description,
                                         vat=self.vat, inventory=self.inventory, admin_id=self.admin_id)
            elif answer == "n":
                print("Exit")
                run_new = False
        breakpoint()


instance_of_products = AllProducts(name=products_info['name'], price=products_info['price'],
                                   description=products_info['description'], vat=products_info['vat'],
                                   inventory=products_info['inventory'], admin_id=products_info['admin_id'])
instance_of_products.add_new_product()
