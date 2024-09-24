mylist_1 = "['mario', 'gino','lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']


def SerializzaLista(lVar) -> str:
    retStr = "["
    for var in lVar:
        retStr += "'"
        retStr += str(var)
        retStr += "',"

    retStr = retStr[:-1]
    retStr += "]"
    return retStr


def DeserializzaLista(sVar) -> list:
    retList = []
    sVar = sVar[1:-1]
    flagApiceOpen = True
    temp = ""
    for c in sVar:
        if c == "'" and flagApiceOpen:
            flagApiceOpen = False
            continue

        if c == "'" and not flagApiceOpen:
            flagApiceOpen = True
            retList.append(temp)
            temp = ""
            continue
        
        if not flagApiceOpen: 
            temp += c

        
    return retList


print(SerializzaLista(mylist_2))
print(DeserializzaLista(mylist_1))
print(DeserializzaLista(SerializzaLista(mylist_2)))