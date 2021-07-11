"""
Напишите функцию, которая будет принимать три числа (a, b, c) и возвращать True, если последняя
цифра произведения a * b равна последней цифре числа c.
"""

def last_dig(a,b,c):
    return (a * b) % 10 == c % 10

print(last_dig(55, 226, 5190))
print(last_dig(12, 215, 2142))