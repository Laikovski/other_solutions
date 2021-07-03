""" Скрыть номе банковской карты"""
# Условие:
# На вход идёт строка с номером карты. Она может иметь внутри себя пробелы, что функция и должна предусматривать.
# Результат — 12 символов * и 4 последних символа от входной строки.
# Пример:
# hidecard("3459 0054 1234 6674") → ************6674
# hidecard("1234567890987654") → ************7654


# 1 solution
def hidden_numbers_1(str):
  rep = str.replace(' ', '')
  return '*' * len(rep[:-4]) + '' + rep[-4:]

print(hidden_numbers_1('3459 0054 1234 6674'))

# 2 solution
def hidden_numbers_1(str):
  return f'{"*" * 12}{str.replace(" ","")[-4:]}'

print(hidden_numbers_1('3459 0054 1234 6674'))


#######################################################################################3
# 1. Создать произвольный список
l = [1,2,3,4,5,5,6,7,8,9,0]
# 2. Добавить новый элемент типа str в конец списка
l.append('new_element')
# 3. Добавить новый элемент типа int на место с индексом
l[3] = 99
# 4. Добавить новый элемент типа list в конец списка
l.append([3,3,3])
# 5. Добавить новый элемент типа tuple на место с индексом
l[0] = (3,3,3)
# 6. Получить элемент по индексу
print(l[1])
# 7. Удалить элемент
l.remove(3)
# 8. Найти число повторений элемента списка
print(l.count(5))
# Получите первый и последний элемент списка
print(l[0],l[-1])
# Поменяйте значения переменных a и b местами
a, b = 1,2
a, b = b, a
# Проверить, есть ли в последовательности дубликаты
l =[1,1,2,2,3,3,4,4,5,5]
s = set(l)
print(len(l)==len(s))
#############################################################
# 1. Создать произвольный словарь
new_dict = {'one': 1, 'two': 2}
# 2. Добавить новый элемент с ключом типа str и значением типа int
new_dict['three'] = 3
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
new_dict[(1,2)] = [1,2,3]
# 4. Получить элемент по ключу
print(new_dict['one'])
print(new_dict.get('two'))
# 5. Удалить элемент по ключу
new_dict.pop('two')
print(new_dict)
# 6. Получить список ключей словаря
print(new_dict.keys())
###########################################################
# Создать множество(set)
new_set = {1,2,2,3,4,5,6}
# 2. Создать неизменяемое множество(frozenset)
second_set = frozenset({7,8,9,2,6})
# 3. Выполнить операцию объединения созданных множеств
print(new_set.union(second_set))
# 4. Выполнить операцию пересечения созданных множеств
print(new_set.intersection(second_set))

####################################################################
"""Ваша цель — написать функцию, которая находит недостающие буквы английского алфавита. 
На вход идут только символы английского языка в нижнем регистре. Возвращаемое значение — строка из недостающих символов.
Пример:
findmissingletters('abc') -> defghijklmnopqrstuvwxyz
findmissingletters('mnopqrstuvwxyz') -> abcdefghijkl
findmissingletters('acegikmoqsuwy') -> bdfhjlnprtvxz"""

from string import ascii_lowercase
#1

# def  findmissingletters(letters):
#   res = ''
#   for i in ascii_lowercase:
#     if i not in letters:
#       res += i
#   return res

# 2
def findmissingletters(l):
  return ''.join(filter(lambda x: x not in l.lower(), ascii_lowercase))

print(findmissingletters('abc'))
print(findmissingletters('mnopqrstuvwxyz'))
print(findmissingletters('acegikmoqsuwy'))