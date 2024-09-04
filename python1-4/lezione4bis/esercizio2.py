#Stampare la lunghezza dell'ultima parola in una frase
print("hello world    baby".split(" "))

def lenLastWorld(s: str):
    return len(s.split(" ")[-1])

print(lenLastWorld("hello world    baby"))
print(lenLastWorld("hello world    "))

def lenLastWorld(s: str):
    l: list[str] = s.split(" ")
    n: int = l.count("")
    for i in range(n):
        l.remove("")
    return(len(l[-1]))

print(lenLastWorld("hello world    baby"))
print(lenLastWorld("hello world         "))

def lenght_of_last_word(s: str) -> int:
    return len(s.strip().split(" ")[-1])

print(lenLastWorld("hello world    baby"))
print(lenLastWorld("hello world         "))