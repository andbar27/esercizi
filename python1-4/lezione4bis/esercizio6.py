#   restituire lista con valori in comuni, senza usare i set, una ripetizione per elemento
def intersection(nums1: list[int], nums2: list[int]):
    ret: list[int] = []
    for n1 in nums1:
        for n2 in nums2:
            if(n1 == n2 and n1 not in ret):
                ret.append(n1)
    return ret

nums1 = [2,2,4,2,1]
nums2 = [1,1,2,0,2,1,2]
print(intersection(nums1,nums2))