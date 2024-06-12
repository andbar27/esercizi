class Contatore:
    
    def __init__(self):
        self.val = 0
        
    def setZero(self):
        self.val = 0
    
    def add1(self):
        self.val += 1
        
    def sub1(self):
        if self.val == 0:
            print("Non è possibile eseguire la sottrazione")
            return
        self.val -= 1
    
    def get(self):
        return self.val
    
    def mostra(self):
        print("Conteggio attuale:", self.val)



class RecipeManager:
    recipes: dict[str:dict[str:list[str]]] = dict()
    
    def __init__(self):
        RecipeManager.recipes = dict()
        pass
    
    @staticmethod
    def create_recipe(name, ingredients):
        if name in RecipeManager.recipes:
            #print("Error")
            return
        
        recipe = dict()
        recipe[name] = ingredients
        RecipeManager.recipes[name] = recipe
        return recipe
        
    @staticmethod
    def add_ingredient(recipe_name, ingredient): 
        if recipe_name not in RecipeManager.recipes:
            #print("Error")
            return
            
        if recipe_name in RecipeManager.recipes:
            if ingredient in RecipeManager.recipes[recipe_name]:
                #print("Error 2")
                return
        
        RecipeManager.recipes[recipe_name][recipe_name] += [ingredient]
        return RecipeManager.recipes[recipe_name]


    @staticmethod
    def remove_ingredient(recipe_name, ingredient): 
        if recipe_name not in RecipeManager.recipes:
            print("Error")
            return
            
        if recipe_name in RecipeManager.recipes:
            if ingredient not in RecipeManager.recipes[recipe_name][recipe_name]:
                print("Error 3")
                return RecipeManager.recipes[recipe_name]
        
        RecipeManager.recipes[recipe_name][recipe_name].remove(ingredient)
        return RecipeManager.recipes[recipe_name]
    
    @staticmethod
    def update_ingredient(recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in RecipeManager.recipes:
                print("Error")
                return
                
        if recipe_name in RecipeManager.recipes:
            if old_ingredient not in RecipeManager.recipes[recipe_name][recipe_name]:
                print("Error 3")
                return RecipeManager.recipes[recipe_name]
        
        i = RecipeManager.recipes[recipe_name][recipe_name].index(old_ingredient)
        RecipeManager.recipes[recipe_name][recipe_name].remove(old_ingredient)
        RecipeManager.recipes[recipe_name][recipe_name].insert(i, new_ingredient)
        return RecipeManager.recipes[recipe_name]
    
    
    @staticmethod
    def list_recipes():
        return list(RecipeManager.recipes.keys())
    
    @staticmethod
    def list_ingredients(recipe_name): 
        if recipe_name not in RecipeManager.recipes:
            #print("Error")
            return
        
        return RecipeManager.recipes[recipe_name][recipe_name]

    @staticmethod
    def search_recipe_by_ingredient(ingredient): 
        retList: dict[str:str] = dict()
        for key, value in RecipeManager.recipes.items():
            if ingredient in value[key]:
                retList[key] = RecipeManager.recipes[key][key]
                
        if list(retList.keys()) == []:
            ""
            #print("Error 4")
        else:
            return retList



class Veicolo:
    
    def __init__(self, marca: str, modello: str, anno: int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        

class Auto(Veicolo):
    
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")


class Specie:
    
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        
    def cresci(self):
        self.popolazione += self.popolazione * (1 + self.tasso_crescita/100)
        #self.popolazione += self.popolazione/100 * self.tasso_crescita
        
    def anni_per_superare(self, altra_specie: object) -> int:
        import copy
        specie = copy.deepcopy(self)
        altra = copy.deepcopy(altra_specie)
        
        anni = 1
        while specie.popolazione < altra.popolazione:
            #specie.cresci()
            specie.popolazione += specie.popolazione/100 * specie.tasso_crescita
            #altra.cresci()
            altra.popolazione += altra.popolazione/100 * altra.tasso_crescita
            anni += 1
            
        return anni
        
    def getDensita(self, area_kmq: float) -> int:
        import copy
        specie = copy.deepcopy(self)
        
        anni:int = 0
        while specie.popolazione / area_kmq < 1:
            specie.cresci()
            anni += 1
            
        return anni
        
        
class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita)
        
        
class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione, tasso_crescita)
            
        
        



class Specie:
    
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        
    def cresci(self):
        self.popolazione += self.popolazione * (1 + self.tasso_crescita/100)
        #self.popolazione += self.popolazione/100 * self.tasso_crescita
        
    def anni_per_superare(self, altra_specie: object) -> int:
        import copy
        #specie = copy.deepcopy(self)
        specie = self
        #altra = copy.deepcopy(altra_specie)
        altra = altra_specie
        
        anni = 1
        while specie.popolazione < altra.popolazione:
            #specie.cresci()
            specie.popolazione += specie.popolazione/100 * specie.tasso_crescita
            #altra.cresci()
            altra.popolazione += altra.popolazione/100 * altra.tasso_crescita
            anni += 1
            
        return anni
        
    def getDensita(self, area_kmq: float) -> int:
        import copy
        #specie = copy.deepcopy(self)
        specie = self
        
        anni:int = 0
        while specie.popolazione / area_kmq < 1:
            specie.cresci()
            anni += 1
            
        return anni
        
        
class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita)
        
        
class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione, tasso_crescita)
            
        
        
# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

"""

def visit_tree(tree: dict[int, list[int]], n: int, count: int, liv: dict[int, list[int]]):
    print(n)
    liv[count].append(n)
    left, right = tree[n]
    if left:
        print("\t"*count,end="")
        visit_tree(tree, left, count+1, liv)
    if right:
        print("\t"*count,end="")
        visit_tree(tree, right, count+1, liv)

tree = {1:[2,3], 2:[4,None], 3:[None,7], 4:[5,6], 5:[None,None], 6:[None,None], 7:[None,None]}
liv = dict()
visit_tree(tree, 1, 1, liv)

#   Ricerca binaria ricorsiva
l = list(range(16))
#print(l)

def binary_search(array, x, count, ret):
    lenArr = len(array)
    midArr = lenArr // 2 
    val = array[midArr]
    if(val == x):
        return midArr, count
    elif(val < x):
        return binary_search(array[midArr+1:lenArr], x, count+1)
    else:
        return binary_search(array[0:midArr], x, count+1)

#   print(binary_search(l, int(input("ricerca questo: ")), 1, 0))



1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione
    specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai 
progettato in sequenza.

Esempio:

construct_rectangle(4)

L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto 
a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2."""
"""
def construct_rectangle(area: float) -> list[float]:
    bestCase = area
    ret = [area, 1]
    L = area
    for w in range(int(area ** 0.5), 0, -1):
        temp = L - w
        if area % w == 0 and temp >= 0 and temp < bestCase :
            L = area // w
            bestCase = temp
            ret = [L,w]
    return ret


import time
start = time.time_ns()
print(construct_rectangle(4))	
print(construct_rectangle(37))
print(construct_rectangle(122122))
print(construct_rectangle(49))
stop = time.time_ns()
print(f"milliSecondi trascorsi: {(stop-start)/10**6}")
"""




"""
prime = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97) + tuple(range(101,570000,2))
def prime_factors(n: int) -> list[int]:
    temp: int = n
    ret: list[int] = []
    j = 0
    while(temp > 1):
        for i in prime[j:]:
            if(temp % i == 0):
                ret.append(i)
                temp //= i
                break
            j+=1
    return ret
"""
"""
def prime_factors(n: int) -> list[int]:
    temp: int = n
    ret: list[int] = []
    j = 2
    while(temp > 1):
        if(temp % j == 0):
            ret.append(j)
            temp //= j
        else:
            j+=1
    return ret

import time
start = time.time_ns()
print(prime_factors(4))
print(prime_factors(60))
print(prime_factors(627))
print(prime_factors(622919))
print(prime_factors(99999999999999999999))
stop = time.time_ns()
print(f"milliSecondi trascorsi: {(stop-start)/10**6}")
"""
