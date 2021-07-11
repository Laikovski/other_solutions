"""
Напишите функцию, которая будет высчитывать время, сэкономленное за счет превышения лимита скорости.
Эта функция будет принимать три числа — лимит скорости, среднюю скорость движения и расстояние,
которое водитель проехал со средней скоростью.

Примечания:

    Скорость = расстояние / время
    Возвращаемое время должно быть в минутах, а не в часах.
    Скорость передается в км/ч, расстояние — в км.
    Сэкономленное время — разница между временем движения при скоростном лимите и при средней скорости.
"""

def time_saved(limit, avg, d):
    return round(abs((d / limit - d / avg) * 60), 1)


print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 40 ))
print(time_saved(80, 100, 10))