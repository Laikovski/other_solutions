"""Задача с решением. «Сумма цифр факториала»
Задача №20 Проект Эйлера.

Условие:
n! означает n × (n − 1) × … × 3 × 2 × 1

Например, 10! = 10 × 9 × … × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
"""


# def factorial(num):
#     f = 1
#     while num > 1:
#         f = f * num
#         num -= 1
#     return sum(int(x) for x in str(f))
#
# print(factorial(10))
#
# def fac_for(num):
#     f1 = 1
#     for i in range(1, num + 1):
#         f1 = f1 * i
#     return f1
#
# print(fac_for(10))










# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return factorial(num-1) * num
#
# print(factorial(5))

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#
#     f1 = 1
#     for i in range(1, num + 1):
#         f1 *= i
#
#     return f1
#
# print(factorial(5))

# def factorial(num):
#
#     res = 1
#     while num > 0:
#         res = res * num
#         num -= 1
#     return res
#
# print(factorial(1005))


# def factorial(num):
#     if num == [0,1]:
#         return 1
#     f1 = 1
#     for i in range(1, num + 1):
#         f1 *= i
#
#     return f1
#
# print(factorial(1))

def factorial(num):
    if num in [0,1]:
        return 1

    return factorial(num - 1) * num

print(factorial(10))
