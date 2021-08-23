#Task_1
def my_gen (odd_nums):
    for nums in range(1, odd_nums + 1, 2):
        yield nums


odd_nums = int(input('enter your number: '))
print(list(my_gen(odd_nums)))