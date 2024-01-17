import database

customers_info = {'name': '<NAME>', 'email': '<email>', 'my_products': '<my_products>', 'amount': '<amount>',
                  'cart_id': '<cart_id>', 'payment_id': '<payment_id>'}


class Customers:
    def __init__(self, name, email, my_products, amount):
        self.name = name
        self.email = email
        self.my_products = my_products
        self.amount = amount

    def add_new_customer(self):
        run_new = True
        print("Please enter new customer")
        while run_new:
            self.name = input("Enter customer's name: ")
            self.email = float(input("Enter customer's email:"))
            self.my_products = input("Enter customer's products:")
            self.amount = float(input("Enter amount of customer's products:"))
            answer = input("Do you want to add another customer? (y/n)")
            if answer == "y":
                database.add_new_customer(name=self.name, email=self.email, my_products=self.my_products,
                                          amount=self.amount)
            elif answer == "n":
                print("Exit")
                run_new = False
        breakpoint()


instance_of_customer_info = Customers(name=customers_info['name'], email=customers_info['email'],
                                      my_products=customers_info['my_products'], amount=customers_info['amount'])
instance_of_customer_info.add_new_customer()