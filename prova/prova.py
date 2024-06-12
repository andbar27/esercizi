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
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero Porte: {self.numero_porte}")


class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")




        

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


"""
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