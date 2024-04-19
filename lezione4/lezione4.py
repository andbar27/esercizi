def subtract(a: float, b: float) -> float:
    return a - b

def check_value(n: int):
    if(n < 5): ret = "minore di 5" 
    elif(n == 5): ret = "uguale a 5" 
    else: ret = "maggiore di 5"
    print(ret)

def check_length(s: str):
    l = len(s)
    if(l < 10): ret = "minore di 10" 
    elif(l == 10): ret = "uguale a 10" 
    else: ret = "maggiore di 10"
    print(ret)

def print_numbers(ln: list[int]):
    for n in ln:
        print(n)

def check_each(ln: list[int]):
    for n in ln:
        check_value(n)

def add_one(n: int) -> int:
    return n+1

def add_one_to_list(ln: list[int]) -> list[int]:
    new_list = [add_one(_) for _ in ln]
    print(new_list)
    return new_list

ln = list(range(8))
print(subtract(5,6))
check_value(4)
check_length("ciaoo")
print_numbers(ln)
check_each(ln)
print(add_one(9))
print(add_one_to_list(ln))


