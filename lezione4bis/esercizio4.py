#in una lista trova il numero presente almeno n//2 +1 volte
def majority_element(l: list[int]) -> int:
    lenght: int = len(l)
    i: int = 0
    lt: list[int] = []
    for n in l:
        if(i > lenght//2):
            return(None)
        if(lt.count(n)):    #diverso da 0
            continue
        if(l.count(n) > lenght // 2):
            return(n)
        lt.append(n)
        i+=1

l: list[int] = [1,1,1,1,2,2,2]
print(majority_element(l))
l.reverse()
print(majority_element(l))
l: list[int] = [1,1,1,2,2,2]
print(majority_element(l))
l: list[int] = [3,2,3]
print(majority_element(l))
l: list[int] = [2,2,1,1,1,2]
print(majority_element(l))