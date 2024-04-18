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