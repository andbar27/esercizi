#Scrivere funzione che ritorni se un intero è palindroma o meno
def is_palindromo(x: int) -> bool:
    pass
    s: str = str(x)
    for i, j in (s, s[::-1]):
        if(i != j):
            return False
    return True

# print(is_palindromo(121))
# print(is_palindromo(-121))

def is_palindromo(x: int) -> bool:
    s: str = str(x)
    lenght: int = len(s) 
    rang: int = lenght // 2
    for i in range(rang):
        if(s[i] != s[lenght-1-i]):
            return False
    return True

print(is_palindromo(121))
print(is_palindromo(-121))
