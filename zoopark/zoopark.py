class Animal:
    def __init__(self, name: str = "Animal", species: str = "Species", age: float = 0.0027,
                 height: float = 0.0, width: float = 0.0,
                 preferred_habitat: str = "Habitat"):
        self.name = name
        self.species = species
        if(age <= 0): 
            age = 0.0027 
        self.age = age
        if(height < 0): 
            height = 0
        self.height = height
        if(width < 0): 
            width = 0
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)
        self.fence = None

    def __str__(self) -> str:
        message = f"name: {self.name} - species: {self.species} - age: {self.age}" \
        + f" height: {self.height}  width: {self.width} - habitat: {self.preferred_habitat}" \
        + f" - health: {self.health}"
        return message

class Fence:
    def __init__(self, animals: list[Animal] = [], area: float = 0,
                 temperature: float = 0, habitat: str = "Habitat"):
        self.animals = animals
        self.idList = id(self.animals)
        #self.animals = animals.copy()  #   serve verificare le condizioni
        if area < 0: area = 0
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

    def __str__(self) -> str:
        message = f"area: {self.area} - temp: {self.temperature} - habitat: {self.habitat}\n"
        for animal in self.animals:
            message += f"\t\t\t{animal}\n"
        return message


class ZooKeeper:
    def __init__(self, name: str = "Name", surname: str = "Surname", id: str = "Id"):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        animalArea = animal.height * animal.width
        if animal.preferred_habitat == fence.habitat:
            if animalArea <= fence.area:
                fence.area -= animalArea
                fence.animals.append(animal)
                animal.fence = fence
        

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            animalArea = animal.height * animal.width
            fence.area += animalArea
            animal.fence = None

    def feed(self, animal: Animal):
        tempHeight = animal.height + (animal.height / 100 * 2)
        tempWidth = animal.width + (animal.width / 100 * 2)
        tempAnimalArea = tempHeight * tempWidth
        animalArea = animal.height * animal.width
        diffAnimalArea = tempAnimalArea - animalArea

        fence = animal.fence

        if diffAnimalArea <= fence.area:
            fence.area -= diffAnimalArea
            animal.height = tempHeight
            animal.width = tempWidth
            animal.health += (animal.health / 100)
        else:
            print(f"The animal {animal.name} is too big for feed it")


    def clean(self, fence: Fence):
        totalAnimalArea = 0
        animals = fence.animals
        for animal in animals:
            areaAnimal = animal.height * animal.width
            totalAnimalArea += areaAnimal
            print(f"tempArea: {animal} - {animal.height} {animal.width} {totalAnimalArea}")
        if fence.area == 0:
            return totalAnimalArea
        areaRatio = totalAnimalArea / fence.area
        return areaRatio

    def __str__(self) -> str:
        message = f"name: {self.name} - surname: {self.surname} - id: {self.id}"
        return message



class Zoo:
    def __init__(self, name: str = "Zoo",
                 fences: list[Fence] = [], 
                 zookeepers: list[ZooKeeper] = []):
        self.name = name
        self.fences = fences
        self.zookeepers = zookeepers
    
    def describe_zoo(self):
        print(self)

    def __str__(self) -> str:
        sepFence = "#" * 30
        message = self.name
        
        message += "\n\n\tList of Fances:\n"
        for fence in self.fences:
            message += f"\t\t{fence}\t\t" + sepFence
        
        message += "\n\tList of Zookeepers:\n"
        for zookeeper in self.zookeepers:
            message += f"\t\t{zookeeper}\n"
        
        return message

"""
a1 = Animal()
a2 = Animal()
zk1 = ZooKeeper()
f1 = Fence()
z1 = Zoo(fences=[f1], zookeepers=[zk1])
zk1.add_animal(a1, f1)
zk1.add_animal(a2, f1)
z1.describe_zoo()
#Done
#print(zk1.clean(f1))
zk1.feed(a1)
#print(a1)
#Done
print("\n\n")
lion = Animal(name = "Leo", species = "Lion", age = 2, height = 4, width = 3)
lionFence = Fence(area = 12.0)
print("created lionFence: \n", lionFence, "\n\n")
# print("clean1: ",zk1.clean(lionFence))
print("add lion to lionFence\n")
zk1.add_animal(lion, lionFence)
# print("clean2 (after add): ",zk1.clean(lionFence))
# print(lion)
# print("feed")
# zk1.feed(lion)

# print(zk1.clean(lionFence))
# print(lion)
# print("clean4: ",zk1.clean(lionFence))

# print("\n\n")
z1.describe_zoo()
"""
a1 = Animal(name="a1")
a2 = Animal(name="a2")
a3 = Animal(name="a3")
a4 = Animal(name="a4")
f1 = Fence()
f2 = Fence()

zk1 = ZooKeeper()
zk1.add_animal(a1, f1)
zk1.add_animal(a2, f1)
zk1.add_animal(a3, f2)
zk1.add_animal(a4, f2)

flag = f1.idList == f2.idList
print("id list f1 == f2 ",flag)

f3 = Fence()
print("id list f1 == f3 ",f3.idList == f1.idList)

f4 = Fence()
print("id list f4 == f3 ",f3.idList == f4.idList)

#CLASSI E METODI UTILIZZATI
"""
class Fence:
    def __init__(self, animals: list[Animal] = [], area: float = 0,
                 temperature: float = 0, habitat: str = "Habitat"):
        self.animals = animals
        self.idList = id(self.animals)
        if area < 0: area = 0
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
"""
"""
class ZooKeeper:
    def __init__(self, name: str = "Name", surname: str = "Surname", id: str = "Id"):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        animalArea = animal.height * animal.width
        if animal.preferred_habitat == fence.habitat:
            if animalArea <= fence.area:
                fence.area -= animalArea
                fence.animals.append(animal)
                animal.fence = fence
        
"""
"""
class Animal:
    def __init__(self, name: str = "Animal", species: str = "Species", age: float = 0.0027,
                 height: float = 0.0, width: float = 0.0,
                 preferred_habitat: str = "Habitat"):
        self.name = name
        self.species = species
        if(age <= 0): 
            age = 0.0027 
        self.age = age
        if(height < 0): 
            height = 0
        self.height = height
        if(width < 0): 
            width = 0
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)
        self.fence = None
"""