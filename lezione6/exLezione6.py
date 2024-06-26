#   Andrea Barbato

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store 
# two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that 
# prints these two pieces of information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open. Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.
import random


class Restaurant:
    def __init__(self, resturant_name: str, cuisine_type: str):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.resturant_name}: {self.cuisine_type}")
    
    def open_restuarant(self):
        print(f"{self.resturant_name} is Open")
    
restaurant = Restaurant("Osteria", "Vecchia Cucina")
print(restaurant.resturant_name, ": ", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restuarant()


# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from 
# the class, and call describe_restaurant() for each instance.
r2 = Restaurant("McD", "Industriale")
r3 = Restaurant("Etnica", "Classica")
for r in [restaurant, r2, r3]:
    r.describe_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then 
# create several other attributes that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information. Make another method called 
# greet_user() that prints a personalized greeting to the user. Create several instances representing 
# different users, and call both methods for each user.
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
    
u1 = User("and", "bar", 27)
u2 = User("luc", "did", 28)
for u in [u1, u2]:
    u.describe_user()
    u.greet_user()


# 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served 
# with a default value of 0. Create an instance called restaurant from this class. Print the number of 
# customers the restaurant has served, and then change this value and print it again. Add a method 
# called set_number_served() that lets you set the number of customers that have been served. Call this 
# method with a new number and print the value again. Add a method called increment_number_served() 
# that lets you increment the number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, a day of business. 
class Restaurant:
    def __init__(self, resturant_name: str, cuisine_type: str, open: bool = False):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = open
    
    def describe_restaurant(self):
        print(f"{self.resturant_name}: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.resturant_name} is Open")
        self.open = True
    
    def close_restaurant(self):
        self.number_served = 0
        self.open = False

    def set_number_served(self, nServed):
        if self.open:
            self.number_served = nServed
    
    def increment_number_served(self, increment = 1):
        if self.open:
            self.number_served += increment
    
    def __str__(self):
        return f"{self.resturant_name}: {self.cuisine_type} - served number: {self.number_served}"

restaurant = Restaurant("Olbia", "Sarda")
print(restaurant.number_served)
restaurant.set_number_served(5)
restaurant.increment_number_served()
print(restaurant.number_served)



# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
u4 = User("Dino", "Va", 22)
u4.increment_login_attempts()
u4.increment_login_attempts()
print(u4.login_attempt)
u4.reset_login_attempts()
print(u4.login_attempt)


# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called 
# IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
# Either version of the class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method. 
class IceCreamStand(Restaurant):
    def __init__(self, resturant_name: str, cuisine_type: str, flavors: list[str], open: bool = False):
        super().__init__(resturant_name, cuisine_type, open)
        self.flavors = flavors
    
    def printFlavors(self):
        for flavor in self.flavors:
            print(flavor)

kalacta = IceCreamStand("Kalacta", "Gelateria", ["limone","pistacchio","crema"])
kalacta.printFlavors()


# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from 
# the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a 
# list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method 
# called show_privileges() that lists the administrator’s set of privileges. Create an instance of 
# Admin, and call your method. 
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: list[str]):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges
    
    def printPrivileges(self):
        for privilege in self.privileges:
            print(privilege)

superuser = Admin("Andrea", "Barbato", 27, ["can delete post", "can add post", "can ban user"])
superuser.printPrivileges()


# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, 
# that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this 
# class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin 
# and use your method to show its privileges.
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

privilege = Privileges(["ban", "add", "remove"])
superuser = Admin("Andrea", "Barbato", 27, privilege)
superuser.privileges.show_privileges()


# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate 
# file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show 
# that the import statement is working properly.
#   done, name file: useRestaurant.py


# 9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and 
# Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
from user0 import *
privilege = Privileges0(["ban","unban","add","remove"])
superU = Admin0("Andrea", "Barbato", 27, privilege)
superU.privileges.show_privileges()



# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes 
# in a separate module. In a separate file, create an Admin instance and call show_privileges() to show 
# that everything is still working correctly.
#   done


# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a 
# method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 
# times.
class Die:
    def __init__(self, sides: int = 6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1,self.sides) 

d6 = Die()
d10 = Die(sides=10)
d20 = Die(sides=20)
for i in range(10):
    print("d6: ",d6.roll_die())
    print("d10: ",d10.roll_die())
    print("d20: ",d20.roll_die())


# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 
# 4 numbers or letters from the list and print a message say  ing that any ticket matching these 4 numbers 
# or letters wins a prize.
lott_str = "a b c d e f g h i l 1 2 3 4 5"
lottery_list = lott_str.split(" ")
print(lottery_list)

def ticket():
    select = []
    while len(select) < 4:
        temp = random.randint(0,14)
        if lottery_list[temp] not in select:
            select.append(lottery_list[temp])
    return select

select = ticket()
print(f"any ticket matching these 4 numbers wins a prize! {select}")
select.sort()
print(select)



# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you 
# just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until 
# your ticket wins. Print a message reporting how many times the loop had to run to give you a winning 
# ticket.
winner_ticket = ticket()
winner_ticket.sort()
print("winner_ticket ",winner_ticket)
i = 1
while True:
    my_ticket = ticket()
    my_ticket.sort()
    print("my ticket ",my_ticket)
    if(my_ticket == winner_ticket):
        print("WIN!!!, attempts: ", i)
        break
    i += 1



