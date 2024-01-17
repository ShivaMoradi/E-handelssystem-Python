import database
admin_info = {'name': '<NAME>', 'email': '<EMAIL>', 'password': '<PASSWORD>'}


class AdminInfo:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def new_admin(self):
        admin_run = True
        while admin_run:
            self.name = input("Enter admin name: ")
            self.email = input("Enter admin Email:")
            self.password = input("Enter password:")
            print("Admin Info created: " + self.name, self.email, self.password)
            answer = input("Do you want to add new admin? y/n")
            if answer == "y":
                database.add_new_admin(name=self.name, email=self.email, password=self.password)
            elif answer == "n":
                print("Exit")
            breakpoint()


admin_instance = AdminInfo(name=admin_info['name'], email=admin_info['email'], password=admin_info['password'])
admin_instance.new_admin()
