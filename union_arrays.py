"""
Напишите функцию, которая создаёт комбинацию двух списков таким образом:

[1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

"""
def union(arr1, arr2):
    if len(arr1) > len(arr2):
        l = len(arr1)
    else:
        l = len(arr2)
    new_arr = []
    i = 0
    while i < l:

        new_arr.append(arr1[i])
        new_arr.append(arr2[i])
        i += 1
    return new_arr
print(union([1,2,3],[11,22,33]))