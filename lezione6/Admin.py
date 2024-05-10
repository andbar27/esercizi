from User import User

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: Privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges