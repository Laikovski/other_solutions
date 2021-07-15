"""Задача с решением. «Сумма цифр факториала»
Задача №20 Проект Эйлера.

Условие:
n! означает n × (n − 1) × … × 3 × 2 × 1

Например, 10! = 10 × 9 × … × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.

Пишите ваше решение в комментариях. Решение будет через 3 часа."""


def factorial(num):
    f = 1
    while num > 1:
        f = f * num
        num -= 1
    return sum(int(x) for x in str(f))

print(factorial(10))

def fac_for(num):
    f1 = 1
    for i in range(1, num + 1):
        f1 = f1 * i
    return sum(int(x) for x in str(f1))

print(fac_for(10))