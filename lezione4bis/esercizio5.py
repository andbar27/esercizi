def move_zeroes(nums: list[int]):
    nZeroes = nums.count(0)
    for i in range(nZeroes):
        nums.remove(0)
        nums.append(0)

nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)