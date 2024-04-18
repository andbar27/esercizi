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
vehicle = ["treno", "auto", "scooter"]
examples = ["Mi piacciono i nuovi hitachi molto moderni come treni", 
            "Adoro le citycar le puoi parcheggiare ovunque", 
            "Che bello evitare il traffico col motorino"]
[print(f"{vehicle[i]}: {examples[i]}") for i in range(len(vehicle))]

#   3-4. Guest List: If you could invite anyone, living or deceased,
#   to dinner, who would you invite? Make a list that includes at least three 
#   people you’d like to invite to dinner. Then use your list to print a message
#   to each person, inviting them to dinner.
guest = ["Da Vinci", "De Rossi", "Di Ventura"]
[print(f"Ciao {_}, vie a cena dai") for _ in guest]



