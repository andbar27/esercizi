class User:
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