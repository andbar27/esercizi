class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []
    
    def addHobby(self, hobby):
        self.hobbies.append(hobby)
    
    def removeHobby(self, hobby):
        if(hobby in self.hobbies):
            self.hobbies.remove(hobby)

    def addHobbies(self, hobbies):
        for hobby in hobbies:
            if(hobby not in self.hobbies):
                self.hobbies += hobby 

    def __str__(self):
        sep = " - "
        return f'{self.name}{sep}{self.age}{sep}{self.hobbies}'

"""
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
if(alice.age < bob.age):
    print(alice)
else:
    print(bob)

luca = Person("Luca M.", 26)
gino = Person("Gino N.", 31)
pino = Person("Pino M.", 32)

people = [alice, bob, luca, gino, pino]

younger = 200
name = ""
for person in people:
    if(person.age < younger):
        younger = person.age
        name = person.name
print(f"{name} - {younger}")

lino = Person("Lino M.", 12)
people.append(lino)
for person in people:
    if(person.age < younger):
        younger = person.age
        name = person.name
print(f"{name} - {younger}")

lino.addHobby("Calcetto")
print(lino)
lino.removeHobby("Calcetto")
print(lino)
"""

class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f"{self.name}: {self.studyProgram} - age {self.age} - gender {self.gender}")

# andrea = Student("Andrea", "FullStack", 27, "M")
# luca = Student("Luca", "Fullstack", 22, "M")
# pino = Student("Pino", "Fullstack", 32, "F")

# for student in [andrea, luca, pino]:
#     student.printInfo()

class Animal:
    
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs
    
    def setLegs(self, legs: int):
        self.legs = legs
    
    def getLegs(self) -> int:
        return self.legs
    
    def __str__(self):
        return f"{self.name}: {self.legs}"
    
# tigre = Animal("Tigre", 4)
# foca = Animal("Foca", 1)

# for animal in [tigre, foca]:
#     print(animal.name)

# foca.legs = 2
# print(foca.legs)
# foca.setLegs(0)
# print(foca.getLegs())

# for animal in [foca, tigre]:
#     print(animal)

class Food:
    def __init__(self, name, price, descr):
        self.name = name
        self.price = price
        self.description = descr
    
    def __str__(self):
        return f"{self.name}: {self.price} -\n\t{self.description}"

pasta = Food("Pasta", 6, "Pasta di grano duro")
pizza = Food("Pizza", 5, "Pizza napoletana")
print(pasta)

class Menu:
    def __init__(self, foods: list[Food] = []):
        self.foods = foods
    
    def addFood(self, food: Food):
        if(food not in self.foods):
            self.foods.append(food)
    
    def removeFood(self, food: Food):
        if(food in self.foods):
            self.foods.remove(food)

    def printPrices(self):
        for food in self.foods:
            print(food.price)
    
    def getAveragePrice(self):
        avg = 0
        count = 0
        for food in self.foods:
            avg += food.price
            count += 1
        return avg / count

    
    def __str__(self):
        ret = ""
        for food in self.foods:
            ret += str(food)
            ret += "\n"
        return ret

menu = Menu([pasta, pizza])
print(menu)
riso = Food("Riso", 3, "Riso basmati")
menu.addFood(riso)
print("\n", menu)
menu.removeFood(riso)
menu.removeFood(riso)
print("\n", menu)
menu.printPrices()
print(menu.getAveragePrice())