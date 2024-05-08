class Animal:
    def __init__(self, name: str = "", species: str = "", age: float = 0.0027,
                 height: float = 0, width: float = 0,
                 preferred_habitat: str = ""):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        if(age == 0): age = 0.0027
        self.health = round(100 * (1 / self.age), 3)
        self.fence = None

    def __str__(self) -> str:
        message = f"name: {self.name} - species: {self.species} - age: {self.age}" \
        + f"height: {self.height}  width: {self.width} - habitat: {self.preferred_habitat}" \
        + f" - health: {self.health}"
        return message

class Fence:
    def __init__(self, animals: list[Animal] = [], area: float = 0,
                 temperature: float = 0, habitat: str = ""):
        self.animals = animals
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

    def __str__(self) -> str:
        message = f"area: {self.area} - temp: {self.temperature} - habitat: {self.habitat}\n"
        for animal in self.animals:
            message += f"\t\t\t{animal}\n"
        return message


class ZooKeeper:
    def __init__(self, name: str = "", surname: str = "", id: str = ""):
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
        tempHeight = animal.height / 100 * 2
        tempWidth = animal.width / 100 * 2
        tempAnimalArea = tempHeight * tempWidth
        animalArea = animal.height * animal.width
        diffAnimalArea = tempAnimalArea - animalArea

        fence = animal.fence

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
        if fence.area == 0:
            return totalAnimalArea
        areaRatio = totalAnimalArea / fence.area
        return areaRatio

    def __str__(self) -> str:
        message = f"name: {self.name} - surname: {self.surname} - id: {self.id}"



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
        message = self.name
        
        message += "\n\n\tlist of fances:\n"
        for fence in self.fences:
            message += f"\t\t{fence}\n"
        
        message += "\n\tlist of zookeepers:\n"
        for zookeeper in self.zookeepers:
            message += f"\t\t{zookeeper}\n"
        
        return message


