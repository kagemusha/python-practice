nums = [1,2,3,4,5]
nums_comp = [ n * 2 for n in nums if n % 2 == 1]
print(nums_comp)

more_nums = [ n ** 2 for n in range(1, 21, 2) if n % 3 == 0]
print(more_nums)