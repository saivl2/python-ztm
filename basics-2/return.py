def total(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    n1 = another_func(num1, num2)
    return n1

n2 = total(3,4)
print(n2)