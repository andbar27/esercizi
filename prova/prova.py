"""
prime = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97) + tuple(range(101,570000,2))
def prime_factors(n: int) -> list[int]:
    temp: int = n
    ret: list[int] = []
    j = 0
    while(temp > 1):
        for i in prime[j:]:
            if(temp % i == 0):
                ret.append(i)
                temp //= i
                break
            j+=1
    return ret
"""
def prime_factors(n: int) -> list[int]:
    temp: int = n
    ret: list[int] = []
    j = 2
    while(temp > 1):
        if(temp % j == 0):
            ret.append(j)
            temp //= j
        else:
            j+=1
    return ret

import time
start = time.time_ns()
print(prime_factors(4))
print(prime_factors(60))
print(prime_factors(627))
print(prime_factors(622919))
print(prime_factors(99999999999999999999))
stop = time.time_ns()
print(f"milliSecondi trascorsi: {(stop-start)/10**6}")