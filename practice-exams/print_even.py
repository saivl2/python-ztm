nums = list(range(1,11))
even_nums = []

def check_even(num):
    return num % 2 == 0

def print_evens(nums):
    for num in nums:
        if check_even(num):
            even_nums.append(num)
    return even_nums

print(print_evens(nums))

