#even numbers from recursion
num_list = [1,2,3,4,5,6,7,8,9,10]

def rec(num_list, result = []):
    if not num_list:
        return
    else:
        first_element = num_list[0]
        if first_element % 2 == 0:
            result.append(first_element)
    rec(num_list[1:])
    return(result)

print(rec(num_list))

#factorial
def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(3))

# fibonacci
def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(7))


# sum of nested lists

lst = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def get_sum(lst, res = 0):
    for i in lst:
        if type(i) == list:
            res = res + get_sum(i)
        else:
            res += i
    return res

print(get_sum(lst))