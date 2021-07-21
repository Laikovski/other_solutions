"""Вычислите первые 100 чисел Фибоначчи. (Напишите код.)"""

# def fibo(num):
#     f1 = 1
#     f2 = 1
#     print(f1, f2, end=' ')
#     while num > 2:
#         f1, f2 = f2, f1 + f2
#         print(f2, end=' ')
#         num -= 1
# fibo(100)

def fibo(num):
    f1 = 1
    f2 = 1
    print(f1, f2, end=' ')
    for i in range(2, num + 1):
        f1, f2 = f2, f1 + f2

        print(f2, end=' ')
    print(f'\nnum fibo {f2}')
fibo(60)


def count(num):
    if num <= 2:
        return 1
    return count(num-1) + count(num-2)

print(count(10))