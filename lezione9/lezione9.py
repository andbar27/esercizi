#   KEY WORD ARGS
def esempio_kwargs(**kwargs):    #passo numero arbitrario di parametri
    #kwargs: keyword args

    if "alpha" in kwargs:
        alpha: float = kwargs["alpha"] #kwargs è come un dizionario 
    
    return alpha

#utilizzo
ret = esempio_kwargs(alpha="a", beta="b", gamma="c")

print(ret)

def esempio_args(*args):    #passo numero arbitrario di parametri
    #args: iterative list args

    if len(args) > 0:
        alpha: float = args[0]
    
    return alpha

#utilizzo
ret = esempio_kwargs(alpha="a", beta="b", gamma="c")

print(ret)

#Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next


def _reverse_list(head: ListNode, retList: list[int]) -> list[int]:
    if head.next:
        _reverse_list(head.next, retList)
        retList.append(head.val)
        return 
    else:
        retList.append(head.val)
        return
    
    
def reverse_list(head: ListNode) -> list[int]:
    retList = []
    _reverse_list(head, retList)
    return retList

# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate 
# secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere 
#         le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente 
#         risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.

def valid_sudoku(board: list[list[str]]) -> bool:
    y = len(board)
    x = len(board[0])
    for i in range(x):
        riga = []
        colonna = []
        for j in range(y):
            elem = board[i][j]
            elemC = board[j][i]
            if elem != "." and elem in riga:
                return False
            riga.append(elem)
            if elem != "." and elem in colonna:
                return False
            colonna.append(elem)
    
    for j in range(y):
        colonna = []
        for i in range(x):
            elem = board[i][j]
            if elem != "." and elem in colonna:
                return False
            colonna.append(elem)
    
    for incI in range(0, 7, 3):
        for incJ in range(0, 7, 3):
            subMatrix = []
            for i in range(1, 4):       #limite superiore = (x+1)//3 +1
                for j in range(1, 4):
                    elem = board[i+incI-1][j+incJ-1]
                    if elem != "." and elem in subMatrix:
                        return False
                    subMatrix.append(elem)
    
    return True

    

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))

board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","2",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","8","9"]]
print(valid_sudoku(board))


# Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato 
# in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.

# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
def word_break(s: str, wordDict: list[str]) -> bool:
    tempS = s
    for word in wordDict:
        while word in tempS:
            tempS = tempS.replace(word,"")
    
    if tempS:
        return False
        
    return True

print(word_break("leetcode",["leet","code"]))

# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
# in genere utilizzando tutte le lettere originali esattamente una volta.

def anagram(s: str, t: str) -> bool:
    tempS = s.lower()
    for c in t:
        tempS = tempS.replace(c.lower(), "")
    
    if tempS:
        return False
    return True

