"""
У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом,
с while-циклом, с рекурсией.
"""
def sum_numbers(arr):
    res = 0
    for i in arr:
        res += i
    return res

print(sum_numbers([2,2,2,4]))

def sum_numbers_two(arr):
    res = 0
    i = 0
    while i < len(arr):
        res += arr[i]
        i += 1
    return res
print(sum_numbers_two([2,2,2,4]))

def sum_numbers_three(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_numbers_three(arr[1:])

print(sum_numbers_three([2,2,2,4]))