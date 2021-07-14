"""Вычислите первые 100 чисел Фибоначчи. (Напишите код.)"""

def fibo(num):
    f1 = 1
    f2 = 1
    print(f1, f2, end=' ')
    while num > 2:
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')
        num -= 1
fibo(100)

