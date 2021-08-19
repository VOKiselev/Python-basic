#Task_2
odd_nums = int(input('enter your number: '))
nums_gen = (nums for nums in range(1, odd_nums + 1, 2))
print(list(nums_gen))