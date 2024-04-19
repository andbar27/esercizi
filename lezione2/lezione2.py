#   Andrea Barbato
#   18/04/2024
print("Hello World")


#   2-3. Personal Message: Use a variable to represent a person’s name, 
#   and print a message to that person. Your message should be simple, 
#   such as, “Hello Eric, would you like to learn some Python today?”
name: str = "Andrea"
message: str = f"Hello {name}, would you like to learn some Python today?"
print(message)

#   2-4. Name Cases: Use a variable to represent a person’s name, 
#   and then print that person’s name in lowercase, uppercase, and title case.
name: str = "AndRea"
print(name.lower())
print(name.upper())
print(name.capitalize())

#   2-5. Famous Quote: Find a quote from a famous person you admire. 
#   Print the quote and the name of its author. 
#   Your output should look something like the following, 
#   including the quotation marks: 
#   Albert Einstein once said, 
#   “A person who never made a mistake never tried anything new.”
author: str = "PopX"
quote: str = "Sono io u femminiell, u femminiell de papà"
message: str = f"{author} once said, \"{quote}\""
print(message)

#   2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
#   represent the famous person’s name using a variable called famous_person.
#   Then compose your message and represent it with a new variable called message.
#   Print your message. 
famous_person: str = "PopX"
quote: str = "Sono io u femminiell, u femminiell de papà"
message: str = f"{famous_person} once said, \"{quote}\""
print(message)

#   2-8. File Extensions: Python has a removesuffix() 
#   method that works exactly like removeprefix().
#   Assign the value 'python_notes.txt' to a variable called filename.
#   Then use the removesuffix() method to display the filename without
#   the file extension, like some file browsers do.
filename: str = "python_notes.txt"
filename_withoutsuffix: str = filename.removesuffix(".txt")
print(filename_withoutsuffix)


#   3-1. Names: Store the names of a few of your friends in a list called names.
#   Print each person’s name by accessing each element in the list, one at a time.
names: list = ["Luca", "Giovanni", "Mariele"]
[print(_) for _ in names]

#   3-2. Greetings: Start with the list you used in Exercise 3-1,
#   but instead of just printing each person’s name,print a message to them.
#   The text of each message should be the same,
#   but each message should be personalized with the person’s name.
[print(f"Ciao {_}, come stai?") for _ in names]

#   3-3. Your Own List: Think of your favorite mode of transportation,
#   such as a motorcycle or a car, and make a list that stores several examples.
#   Use your list to print a series of statements about these items,
#   such as “I would like to own a Honda motorcycle.”
examples = ["Mi piacciono i nuovi hitachi molto moderni come treni", 
            "Adoro le citycar le puoi parcheggiare ovunque", 
            "Che bello evitare il traffico col motorino"]
[print(_) for _ in examples]

#   3-4. Guest List: If you could invite anyone, living or deceased,
#   to dinner, who would you invite? Make a list that includes at least three 
#   people you’d like to invite to dinner. Then use your list to print a message
#   to each person, inviting them to dinner.
guest = ["Da Vinci", "De Rossi", "Di Ventura"]
invited = [f"Ciao {_}, vieni a cena dai" for _ in guest]
print(invited)

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. 
    Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it 
    with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
guest = ["Da Vinci", "De Rossi", "Di Ventura"]
invited = [f"Ciao {_}, vieni a cena dai" for _ in guest]
print(invited)
print("Da Vinci")
invited[0].replace("Da Vinci", "Gilberto")
[print(_) for _ in invited]

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
    informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
guest = ["Da Vinci", "De Rossi", "Di Ventura"]
invited = [f"Ciao {_}, vieni a cena dai" for _ in guest]
print(invited)
print("Grande tavolo: grande festa")
new_guest = ["Pino","Gino","Lino"]
guest += new_guest
invited.insert(0, f"Ciao {new_guest[0]}, vieni a cena dai")
invited.insert(2, f"Ciao {new_guest[len(invited)//2]}, vieni a cena dai")
invited.append(f"Ciao {new_guest[2]}, vieni a cena dai")
[print(_) for _ in invited]

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time 
for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying 
    that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
    Each time you pop a name from your list, print a message to that person 
    letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know 
    they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
    Print your list to make sure you actually have an empty list at the end of your program.
"""
print("tavolo grande in ritardo, vi caccio tutti tranne 2")
for i in range(len(invited)-2):
    print(f"sorry {guest[-1]}, ti devo cacciare")
    invited.pop()
    guest.pop()
for g in guest:
    print(f"{g}, sei ancora invitato, daje")
del(guest)
# try:
#     print(guest)
# except ValueError:
#     print("la lista è vuota")

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; 
    just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order 
    of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. 
    Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. 
    Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. 
    Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
    Print the list to show that its order has changed.
"""
places = ["Lucca", "Rieti", "Pisa", "Ravenna", "Milano"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
"""
guest = ["Da Vinci", "De Rossi", "Di Ventura"]
invited = [f"Ciao {_}, vieni a cena dai" for _ in guest]
print(invited)
print(f"numero invitati: {len(invited)}")

"""
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, 
or anything else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.
"""
flag = True
myList = []
print("type exit() to exit")
while(flag):
    data = input()
    if(data == "exit()"):
        flag = False
        continue
    if(data[0] == 'a'):
        data.capitalize()
    elif(data[0] == 'b'):
        data.upper()
    else:
        data.lower()
    if(data.find(".txt") != -1):
        data.removesuffix(".txt")
    if(data.find("merda") != -1):
        data.replace("merda", "cacca")
    if(data[0] == "z"):
        myList.append(data)
    else:
        myList.insert(data)
    print(data)
print(myList)    
tempList = sorted(myList)
if(tempList[0][0] == "r"):
    myList.reverse()
else:
    myList.sort()
print(myList)  
