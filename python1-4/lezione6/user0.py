class User0:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0
    
    def describe_user(self):
        print(f"user: {self.first_name} {self.last_name}: {self.age}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0

class Privileges0:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin0(User0):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: Privileges0):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges