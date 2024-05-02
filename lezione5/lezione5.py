#Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
def countdown(n: int) -> int:
    for i in range(n, -1, -1):
        print(i)

countdown(5)

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers) 
    
#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
#mantenendo l'ordine originale degli elementi.
def remove_duplicates(l):
    retL =  []
    for elem in l:
        if(elem not in retL):
            retL.append(elem)
    return(retL)

#Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a 
#seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro 
#to_fahrenheit.
def convert_temperature(degree: float, flag: bool = True) -> float:
    if(flag):
        return degree * 9 / 5 + 32
    return (degree - 32) * 5 / 9

"""
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta 
per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera 
o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" 
oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if(conditionA or (conditionB and conditionC)):
        return "Operazione permessa" 
    return("Operazione negata")

"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato 
k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene 
spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. 
Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni 
sia maggiore della lunghezza della lista.
"""
def rotate_left(elements: list, k: int) -> list:
    lenEl = len(elements)
    modLen = k % lenEl
    kk = modLen - lenEl
    return elements[kk:] + elements[:kk]

"""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""
def check_parentheses(expression: str) -> bool:
    countIndex = []
    lenStr = len(expression)
    for i in range(lenStr):
        flag = False
        if(expression[i] == '('):
            for j in range(i+1, lenStr):
                if(expression[j] == ')' and (j not in countIndex)):
                    countIndex.append(j)
                    flag = True
                    break
            if(flag == False):
                return False
    return True

"""
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista 
di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra 
da elementi uguali.
"""
def count_isolated(nums: list[int]) -> int:
    count = 0
    lenNums = len(nums)
    for i in range(lenNums):
        n = nums[i]
        j = (i + 1) % lenNums
        if(nums[i-1] != n and nums[j] != n):
            count +=1
    return count

"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.
"""
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    retList = set(original_set.copy())
    for elem in elements_to_remove:
        if elem in original_set:
            retList.remove(elem)
    return retList

"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, 
somma i loro valori."""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    retDict = dict()
    for key1, value1 in dict1.items():
        retDict[key1] = value1
    for key2, value2 in dict2.items():
        if key2 in dict1:
            retDict[key2] += value2
        else:
            retDict[key2] = value2
    return retDict