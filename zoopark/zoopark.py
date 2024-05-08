class Animal:
    def __init__(self, name: str, species: str, age: int,
                 height: float, width: float,
                 preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)

    def __str__(self) -> str:
        pass
        

class Fence:
    def __init__(self, animals: list[Animal], area: float,
                 temperature: float, habitat: str):
        self.animals = animals
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

    def __str__(self) -> str:
        pass

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        animalArea = animal.height * animal.width
        if animal.preferred_habitat == fence.habitat:
            if animalArea <= fence.area:
                fence.area -= animalArea
                fence.animals.append(animal)
        

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            animalArea = animal.height * animal.width
            fence.area += animalArea

    def feed(self, animal: Animal):
        tempHeight = animal.height / 100 * 2
        tempWidth = animal.width / 100 * 2
        tempAnimalArea = tempHeight * tempWidth
        animalArea = animal.height * animal.width
        diffAnimalArea = tempAnimalArea - animalArea

        fence = Fence([], 5, 5, "") 
        # Cerca recinto in cui è animal

        if diffAnimalArea <= fence.area:
            fence.area -= diffAnimalArea
            animal.height = tempHeight
            animal.width = tempWidth
            animal.health += (animal.health / 100)


    def clean(self, fence: Fence):
        totalAnimalArea = 0
        animals = fence.animals
        for animal in animals:
            areaAnimal = animal.height * animal.width
            totalAnimalArea += areaAnimal

        areaRatio = totalAnimalArea / fence.area
        if(areaRatio > 0):
            return areaRatio
        return totalAnimalArea

    def __str__(self) -> str:
        pass



class Zoo:
    def __init__(self, fences: list[Fence], 
                 zookeepers: list[ZooKeeper], 
                 name: str = "Zoo"):
        self.name = name
        self.fences = fences
        self.zookeepers = zookeepers
    
    def describe_zoo(self):
        print(self)

    def __str__(self) -> str:
        message = self.name
        
        message += "\n\n\tlist of fances:\n"
        for fence in self.fences:
            message += f"\t\t{fence}\n"
        
        message += "\n\tlist of zookeepers:\n"
        for zookeeper in self.zookeepers:
            message += f"\t\t{zookeeper}\n"
        
        return message


