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

#   [0 - 1 - 2 - 3]     len = 4 len//2 = 2  last control i = 1
#   [0 - 1 - 2 - 3 - 4] len = 5 len//2 = 2  last control i = 1 - 2 non c'è bisogno perché è uguale

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
