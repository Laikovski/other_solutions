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



