def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(3))

def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(7))