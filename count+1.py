"""
Условие:

Ваша задача — написать функцию, которая проверит, все ли значения увеличиваются на один

Пример:
increasing([-1, 0, 1, 2, 3]) -> True
increasing([-1, 0, 1, 3, 4])) -> False
increasing([0, 1]) -> True
increasing([1, 0]) -> False
"""

def increasing(arr):
    for i in range(len(arr)-1):
        if arr[i] + 1 != arr[i+1]:
            return False
    else: return True

print(increasing([-1, 0, 1, 2, 6]))
print(increasing([-1, 0, 1, 3, 4]))
print(increasing([0, 1]))
print(increasing([1, 0]))