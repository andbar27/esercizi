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

"""
Write a function called create_playlist() that accepts a playlist name and a variable number of song 
titles. The function should return a dictionary with the playlist name and a set of songs. 
Call the function with different numbers of songs to demonstrate flexibility.

Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean 
value indicating whether it is liked (True or False). This function should return an updated 
dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)
"""
def create_playlist(name: str, songs: list[str]) -> dict:
    playlist = {name: set()}
    for song in songs:
        playlist[name].add(song)
    return playlist

def add_like(likeDict: dict, album: str, liked: bool = True):
    retDict = dict()
    retDict[album]= likeDict[album]
    retDict["liked"] = liked
    return retDict

playlist = create_playlist("bugiardo", ("a","b","c","d"))
print(playlist)
print(add_like(playlist, "bugiardo"))

"""
Write a function called add_book() that accepts an author's name and a variable number of book titles 
authored by them. This function should return a dictionary where the author's name is the key and the 
value is a list of their books. Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom 
to remove all details. This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)
"""
def add_book(author: str, books: list[str]) -> dict:
    retDict = {author: set()}
    for book in books:
        retDict[author].add(book)
    return retDict

def delete_book(dictionary: dict, author: str) -> dict:
    import copy
    retDictionary = copy.deepcopy(dictionary)
    if(author in dictionary):
        retDictionary.pop(author)

books = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
print(books)
print(delete_book(books, "Mark Twain"))

"""
Write a build_profile() function that accepts the name , surname,  occupation, location, and age  
of a person. Make occupation, location, and age optional parameters. 
Use this function to create profiles for different people, demonstrating how it handles these 
optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
"""
def build_profile(name: str, sourname: str, 
                  occupation: str = None, location: str = None, age: int = None) -> dict:
    profile = {"name": name, "sourname": sourname, 
               "occupation": occupation, "location": location, "age": age}
    return profile

"""
Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
The function should return a dictionary that includes the event name and a list of the participants. 
Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to 
modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)
"""
def plan_event(name: str, partecipants: list[str], hour: str) -> dict:
    event = {"name": name,
             "partecipants": partecipants,
             "hour": hour}
    return event

def modify_event(event: dict, eventName: str, newPartecipants: list[str], newHour: str):
    if eventName == event["name"]:
        event["partecipants"] = newPartecipants
        event["hour"] = newHour

event = plan_event("Code Workshop", ["Alice", "Bob", "Charlie"], "4pm")
print(event)
modify_event(event, "Code Workshop", ["Alice", "John", "Charlie"], "4pm")
print(event)

"""
Write a function called create_shopping_list() that accepts a store name and any number of items as 
arguments. It should return a dictionary with the store name and a set of items to buy there. 
Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints 
each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")
"""
def create_shopping_list(storeName: str, shoppingList: set) -> dict:
    retDict = {storeName: set(shoppingList)}
    return retDict

def print_shopping_list(shoppingDict: dict, storeName: str):
    if storeName in shoppingDict:
        print(f"shopping list of {storeName}:")
        for item in shoppingDict[storeName]:
            print("\t",item)

myShopList = create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
print_shopping_list(myShopList, "Grocery Store")