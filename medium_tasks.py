"""
Ваша задача — написать функцию, которая принимает неограниченное количество массивов
и возвращает только те элементы, что есть в каждом списке.
"""

def find_values(*args):
    return list(set.intersection(*map(set,args)))

print(find_values([11, 10, 3], [10, 3, 5, 11], [11, 10]))
find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"])
find_values([1, 4, 3], [6, 2, 8], ["4", "hi"])