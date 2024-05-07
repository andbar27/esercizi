class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def toString(self):
    #     sep = " - "
    #     return self.name + sep + str(self.age)

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
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