"""
Задание: Напишите функцию, которая будет принимать целое положительное число и определять,
делится ли оно нацело на сумму цифр этого числа.
"""
# def is_divisible(num):
#     suma = 0
#     for i in str(num):
#         suma += int(i)
#     if num % suma == 0:
#         return True
#     else:
#         return False

def is_divisible(num):
    sum_ = sum(map(int, str(num)))
    return  num % sum_ == 0

print(is_divisible(481))
print(is_divisible(89))
print(is_divisible(516))
print(is_divisible(200))