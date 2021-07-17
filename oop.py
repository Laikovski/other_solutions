"""
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}»
в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».


"""

class Soda:
    def __init__(self, adding):
        if isinstance(adding, str):
            self.adding = adding
        else:
            self.adding = None


    def show_my_drink(self):
        if self.adding:
            print(f'Газировка и {self.adding}')
        else:
            print('Обычна газировка')

n = Soda('foo')
k = Soda(None)
# n.show_my_drink()
# k.show_my_drink()

'''
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
'''


class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'


# Тесты
# triangle1 = TriangleChecker([2, 3, 4])
# print(triangle1.is_triangle())
# triangle2 = TriangleChecker([77, 3, 4])
# print(triangle2.is_triangle())
# triangle3 = TriangleChecker([77, 3, 'Сторона3'])
# print(triangle3.is_triangle())
# triangle4 = TriangleChecker([77, -3, 4])
# print(triangle4.is_triangle())

"""
Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, 
а с помощью метода to_pounds() они переводятся в фунты. Чтобы закрыть доступ к переменной “kg” она 
реализовала методы set_kg() - для задания нового значения килограммов, get_kg()  - для вывода текущего значения кг.
Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений. 
Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.
"""


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы задаются только числами')


# Тесты
# weight = KgToPounds(12)
# print(weight.to_pounds())
# print(weight.kg)
# weight.kg = 41
# print(weight.kg)
# weight.kg = 'десять'




# Создайте класс Point. У этого класса должны быть метод set_coordinates, который принимает координаты по x и по y,
# и сохраняет их в экземпляр класса соответственно в атрибуты x и y метод get_distance, который обязательно
# принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение
# "Передана не точка"
#
# Пример работы с классом Point
#
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"


import math

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')


# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"


"""
Создайте класс Laptop, у которого есть:

конструктор __init__, принимающий 3 аргумента: brand, model, price . Также во время инициализации необходимо
создать атрибут laptop_name - строковое значение, вида "<brand> <model>"

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.laptop_name) # выводит "hp 15-bw0xx"

И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.
"""
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'

hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.laptop_name) # выводит "hp 15-bw0xx"

"""


Создайте класс SoccerPlayer, у которого есть:

    1. конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо создать 
    2 атрибута экземпляра: goals и assists - общее количество голов и передач игрока, изначально оба значения 
    должны быть 0 
    2. метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение 
    равно единице. Метод должен увеличить общее количество забитых голов игрока на переданное значение;
    3. метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное 
    значение равно единице. Метод должен увеличить общее количество сделанных передач игроком на переданное 
    значение;  
    4. метод statistics, который вывод на экран статистику игрока в виде:

        <Фамилия> <Имя> - голы: <goals>, передачи: <assists>



"""

class SoccerPlayer:

    def __init__(self, name, username, goals=0, assists=0):
        self.name = name
        self.username = username
        self.goals = goals
        self.assists = assists

    def score(self, goals = 1):
        self.goals += goals

    def make_assist(self, assists = 1):
        self.assists += assists

    def statistics(self):
        print(f'{self.username} {self.name} - голы: {self.goals}, передачи: {self.assists}')


# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"


"""
Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая",
 "Полоска черная", начиная именно с фразы "Полоска белая"

"""

class Zebra:
    def __init__(self, count=0):
        self.count = count
    def which_stripe(self):
        if self.count % 2 == 0:
            print("Полоска белая")
            self.count += 1
        else:
            print("Полоска черная")
            self.count += 1

# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"

"""

 Создайте класс Person, у которого есть:

    конструктор __init__, принимающий 3 аргумента: first_name, last_name, age. 
    метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
    метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;

"""
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

# p1 = Person('Jimi', 'Hendrix', 17)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"

"""
 Создайте класс Dog, у которого есть:

    конструктор __init__, принимающий 2 аргумента: name, age. 
    метод description, который возвращает строку в виде "<name> is <age> years old"
    метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";

"""

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
jack = Dog("Jack", 4)

# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

"""
Ваша задача реализовать класс Stack, у которого есть:

    - метод __init__  создаёт новый пустой стек. Параметры данный метод не принимает. Создает атрибут 
    экземпляра values, где будут в дальнейшем хранятся элементы стека в виде списка (list), 
    изначально при инициализации задайте значение атрибуту values равное пустому списку;
    - метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.
    - метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. 
    Стек изменяется. Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение 
    "Empty Stack";
    - метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, 
    стек не модифицируется. Если элементов в стеке нет, распечатайте сообщение "Empty Stack", 
    верните None после этого;
    - метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
    - метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.


"""
class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            return 'Empty Stack'
        else:
            return self.values.pop()

    def peek(self):
        if len(self.values) == 0:
            print('Empty Stack')
        else:
            return self.values[-1]

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.values)
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2

"""
Создайте класс UserMail, у которого есть:

    конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. Их необходимо сохранить в экземпляр 
    как атрибуты login и __email (обратите внимание, защищенный атрибут)
    метод геттер get_email, которое возвращает защищенный атрибут __email ;
    метод сеттер set_email, которое принимает в виде строки новую почту. Метод должен проверять, что в новой почте 
    есть только один символ @ и после нее есть точка. Если данные условия выполняются, новая почта сохраняется в 
    атрибут __email, в противном случае выведите сообщение "Ошибочная почта";
    создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

"""

class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return f'{self.__email}'

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@') == 1 and '.' in new_email[new_email.find('@'):]:
            self.__email = new_email
        else:
            print("Ошибочная почта")
    email = property(fget=get_email, fset=set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait