def subtract(a: float, b: float) -> float:
    return a - b

def check_value(n: int):
    if(n < 5): ret = "minore di 5" 
    elif(n == 5): ret = "uguale a 5" 
    else: ret = "maggiore di 5"
    print(ret)

def check_value2  (n: int, check: int):
    if(n < check): ret = "minore di 5" 
    elif(n == check): ret = "uguale a 5" 
    else: ret = "maggiore di 5"
    print(ret)

def check_length(s: str):
    l = len(s)
    if(l < 10): ret = "minore di 10" 
    elif(l == 10): ret = "uguale a 10" 
    else: ret = "maggiore di 10"
    print(ret)

def print_numbers(ln: list[int]):
    for n in ln:
        print(n)

def check_each(ln: list[int]):
    for n in ln:
        check_value(n)

def add_one(n: int) -> int:
    return n+1

def add_one_to_list(ln: list[int]) -> list[int]:
    new_list = [add_one(_) for _ in ln]
    print(new_list)
    return new_list

ln = list(range(8))
print(subtract(5,6))
check_value(4)
check_length("ciaoo")
print_numbers(ln)
check_each(ln)
print(add_one(9))
print(add_one_to_list(ln))

"""
8-1. Message: Write a function called display_message() that prints one sentence telling 
everyone what you are learning about in this chapter. Call the function, and make sure 
the message displays correctly.
"""
def display_message():
    print("I learn the function, yeah")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, 
title. The function should print a message, such as "One of my favorite books is Alice in 
Wonderland". Call the function, making sure to include a book title as an argument in the 
function call.
"""
def favorite_book(title: str):
    print(f"My favorite book is {title}")
favorite_book("Alice in Wonderland")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a 
message that should be printed on the shirt. The function should print a sentence 
summarizing the size of the shirt and the message printed on it. Call the function once 
using positional arguments to make a shirt. Call the function a second time using keyword 
arguments.
"""
def make_shirt(size: str, text: str):
    print(f"Size: {size} - Text Message: {text}")
make_shirt("M", "Bella Ciao")
size = input("Insert Size: ")
text = input("Insert Message: ")
make_shirt(size, text)

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with 
a message that reads I love Python. Make a large shirt and a medium shirt with the default 
message, and a shirt of any size with a different message.
"""
def make_shirt(size: str = "L", text: str = "I love Python"):
    print(f"Size: {size} - Text Message: {text}")
make_shirt()
make_shirt(size = "M")
make_shirt(size = "S")
make_shirt(size = "M", text = "bella")
make_shirt(size = "S", text = "ciao")
make_shirt(text = "ao")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and 
its country. The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. Call your function for three different 
cities, at least one of which is not in the default country.
"""
def describe_city(city, country: str = "Italy"):
    print(f"{city} is in {country}")
describe_city("Roma")
describe_city("Milano")
describe_city("London", country = "England")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city 
and its country. The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are 
returned.
"""
def city_country(city: str, country: str):
    print(f"{city}, {country}")
city_country("Roma", "Italia")
city_country("San Marino", "San Marino")
city_country("Santiago", "Chile")

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music 
album. The function should take in an artist name and an album title, and it should return 
a dictionary containing these two pieces of information. Use the function to make three 
dictionaries representing different albums. Print each return value to show that the  
dictionaries are storing the album information correctly. Use None to add an optional 
parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s 
dictionary. Make at least one new function call that includes the number of songs on an 
album.
"""
def make_album(artist: str, album_title: str, nTrack: int = None):
    album = dict(Artist = artist, AlbumTitle = album_title)
    if(nTrack != None or nTrack != ""):
        album["Number-of-Track"] = nTrack
    return album
print(make_album("Annalisa", "Bellissima"))
print(make_album("Franco126", "Stanza Singola", 12))

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows 
users to enter an album’s artist and title. Once you have that information, call make_album()
with the user’s input and print the dictionary that’s created. Be sure to include a quit 
value in the while loop.
"""
flag = True
list_album = []
while(flag):
    cmd = input("For exit write exit: ")
    if(cmd.lower() == "exit"):
        flag = False
        continue
    artist = input("insert artist: ")
    nameAlbum = input("insert name of the album: ")
    nTrack = int(input("insert num of Track: "))
    album = make_album(artist, nameAlbum, nTrack)
    list_album.append(album)
    print(album)

"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a 
function called show_messages(), which prints each text message.
"""
short_message = ["ciao", "bella", "ao"]
def show_message(messageList):
    for message in messageList:
        print(message)

"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a 
function called send_messages() that prints each text message and moves each message to a 
new list called sent_messages as it’s printed. After calling the function, print both of 
your lists to make sure the messages were moved correctly.
"""
sent_messages = []
def send_message(message):
    print(message)
    sent_messages.append(message)

send_message(short_message)
print()
show_message(sent_messages)
print("=")
show_message(short_message)

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function 
send_messages() with a copy of the list of messages. After calling the function, print both 
of your lists to show that the original list has retained its messages.
"""
send_message(short_message)
show_message(sent_messages)

"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call 
provides, and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""
def sandwiches(item_list):
    for item in item_list:
        print(item)
sandwiches(["cotto", "formaggio"])
sandwiches(["cotto", "formaggio", "maionese"])
sandwiches(["cotto", "formaggio", "maionese", "insalata"])

"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your 
first and last names and three other key-value pairs that describe you. All the values must 
be passed to the function as parameters. The function then must return a string such as 
"Eric Crow, age 45, hair brown, weight 67"
"""
def build_profile(name, age, hair, weight):
    print(f"{name}, age {age}, hair {hair}, weight: {weight}")
build_profile("Andrea Barbato", 27, "Dark Brown", 173)

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. Your function should work for a call like this one: 
car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary 
that’s returned to make sure all the information was stored correctly. 
"""
def make_car(manufacturer, model, color = "grey", tow_package = True):
    car = {"manufacturer": manufacturer,
           "model": model,
           "color": color,
           "tow_package": tow_package}
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate 
file called printing_functions.py. Write an import statement at the top of printing_models.py,
and modify the file to use the imported functions.
"""
#ok

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in
a separate file. Import the function into your main program file, and call the function 
using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn:
from module_name import *
"""
import printing_function
from printing_function import printing_models
from printing_function import printing_models as fn
#import printing_function as mn
#from printing_function import *
#mn.printing_models()
printing_models()

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure
they follow the styling guidelines described in this section.
"""
#ok



#OPZIONALI
"""
School Grading System:

    Create a function that takes a student's name and their scores in different subjects as 
    input.
    The function calculates the average score and prints the student's name, average, 
    and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function 
    for each student.
"""
def averageScore(student: str, scores: list[int]) -> int:
    average = sum(scores) // len(scores)
    print(f"{student}'s average: {average}")
    if(average >= 60):
        print("Passed the Exam")
    else:
        print("Fallied the Exam")

"""
2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is 
    too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum 
    number of attempts.
"""
def numberGames(maxNum: int, attempts: int): 
    import random
    generateNumber = random.randint(0, maxNum)
    for attempt in range(attempts):
        tryNum = int(input("try to got the number: "))
        if(tryNum == generateNumber):
            print(f"You got the number!! Is {tryNum}")
            return
    print("Finish attempts.")

"""
3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create a function that manages the shopping cart, allowing the user to add, remove, 
    and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
    Implement a for loop to iterate over the items in the cart and print detailed 
    information about each product and the total.
"""

"""
4. Text Analysis:
    Create a function that reads a text file and counts the number of occurrences of each 
    word.
    The function should print a report showing the most frequent words and their number 
    of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store 
    the occurrences.
    Implement error handling to handle missing files or other input issues.
"""

"""
5. Inventory Management System:
    Create a function that defines an item with a code, name, quantity, and price.
    Create a database or dictionary to store the items in inventory.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops and conditional statements to manage the various inventory operations.
"""

"""
6. Password Generator:

    Create a function that generates a random password with a specified length and desired 
    character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.
"""

"""
7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman 
    numeral.
"""

"""
8. ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.
"""

"""
9. Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
    Handle both encryption and decryption using the same function with appropriate 
    adjustments.
    Encrypt and decrypt the given message using the specified shift value.
"""

"""
10. Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.
"""

"""
11. Word Search Puzzle Solver:

    Create a function that solves a word search puzzle.
    Provide a 2D grid representing the puzzle and a list of words to find.
    Implement a backtracking algorithm to search for the words in the grid, marking visited 
    cells to avoid repetition.
    Output the locations of the found words within the grid.
"""

"""
12. Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers up to a specified limit using 
    the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime 
    initially.
    Iterate through the array, starting from 2, and mark every multiple of the current 
    number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.
"""

"""
13. Fractal Tree Generator:

    Create a function that generates a fractal tree using recursion.
    Specify the starting trunk length and branching angle.
    Draw the trunk and then recursively call the function to draw two branches at the 
    specified angle, each with a shorter length.
    Repeat the branching process until a desired level of detail is reached.
"""

"""
14. Sudoku Solver:

    Create a function that solves a Sudoku puzzle using backtracking.
    Provide a 9x9 grid representing the puzzle with some numbers filled in and others left 
    blank.
    Implement a backtracking algorithm to check for valid placements in empty cells, 
    ensuring no row, column, or 3x3 subgrid contains duplicates.
    Solve the puzzle by filling in the remaining empty cells with valid numbers.
"""

"""
15. Text Editor with Basic Functionality:

    Create a simple text editor that allows the user to open, edit, and save text files.
    Implement basic functionality such as inserting, deleting, and copying text.
    Provide undo/redo functionality to allow users to reverse actions.
    Save the edited text to a file when the user chooses to save.
"""
