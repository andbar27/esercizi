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


print("\n\n ex Tree")
# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

# La lista di interi è formata così:

#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, 
#         significa che il nodo che corrisponde a quell'indice è una foglia.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tuple List with (index, value) compare only the values and verify it's symmetric
# Need to compare the index
# Forse sarebbe meglio usare un dizionario invece della tupla cercando l'indice
# simmetrico corrispondente come chiave e verificandone la presenza, invece di un 
# confronto "posizionale"
def is_symmetric_List_of_Tuple(myList: list[(int, int)]) -> bool:
    lenL = len(myList)

    for i in range(lenL // 2):
        if myList[i][1] != myList[-(i + 1)][1]:
            return False
        
    return True

def symmetric(tree: list[int]) -> bool:

    tempTree = []                   #   Radice
    tempTree.append((0, tree[0]))   #

    matrixTree = []                 #   Matrice che simula l'albero
    matrixTree.append(tempTree)     #   cresce di 2**i

    lenT = len(tree)
    j = 0
    while(tempTree):
        tempTree = []
        for i, node in matrixTree[j]:
            iSx = 2 * i + 1
            iDx = 2 * (i + 1)
            if node:
                if iSx < lenT:
                    tempTree.append((iSx, tree[iSx]))
                if iDx < lenT:
                    tempTree.append((iDx, tree[iDx]))

        matrixTree.append(tempTree)
        print(tempTree)
        if is_symmetric_List_of_Tuple(tempTree) == False:
            return False
        j += 1
    
    print("\n\n\nMatrix Tree complete:")
    for riga in matrixTree:
        print(riga)
    
    return True

def _symmetric(tree: list[int]):
    pass

print("Expected output: True")
print(symmetric([1,2,2,3,4,4,3]), "\n")
print("Expected output: False")
print(symmetric([1,2,2,3,4,4,2]), "\n")
print("Expected output: False")
print(symmetric([1,2,2,3,4,4,3,None,3,None,None,None,None,None,None]), "\n")
print(symmetric([1,2,2,3,4,4,3,3,None,None,None,None,None,None,3,2,2,None,None]), "\n")