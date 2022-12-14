"""Задача 3. Мега-калькулятор
Кеша учится в третьем классе, и уже умеет программировать на питоне. Как и многие его одноклассники, он очень любит сразу применять все полученные знания на практике. Вчера Кеша узнал про модуль math и его основные возможности, поэтому решил написать мега-калькулятор, который бы применял сразу все функции к введенному пользователем числу. Чтобы ничего не забыть, он пользуется шпаргалкой, которую прикрепили к уроку

Напишите программу, которая получает от пользователя вещественное число, по очереди применяет к нему функции модуля Math и выводит результат:

округляет вниз
округляет вверх
берет модуль числа
извлекает квадратный корень
возводит экспоненту в степень, равную числу
считает натуральный логарифм числа
считает логарифм числа по основанию 2
считает логарифм числа по основанию 10
считает синус и косинус числа
И так как Кеша самый умный в классе, он решил попробовать посчитать факториал числа. Для этого ему пришлось придумать и реализовать контроль ввода: факториал вычисляется, только если введенное число было натуральным.
"""

import math

number = float(input('Введите число: '))

floor = math.floor(number)
print('Округление вниз:', floor)

ceil = math.ceil(number)
print('Округление вверх:', ceil)

absNumber = abs(number)
print('модуль числа:', absNumber)

sqrt = math.sqrt(number)
print('извлекает квадратный корень:', sqrt)

exp = math.exp(number)
print('экспонента в степень, равную числу:', exp)

log = math.log(number)
print('натуральный логарифм числа:', log)

log2 = math.log2(number)
print('натуральный логарифм числа по 2:', log2)

log10 = math.log10(number)
print('натуральный логарифм числа по 10:', log10)

cos = math.cos(number)
print('косинус:', cos)

sin = math.sin(number)
print('синус:', sin)

if number == int(number):
  factorial = math.factorial(number)
  print('Факториал:', factorial)