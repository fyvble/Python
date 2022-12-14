"""Задача 1. Герон
Существует, так называемая, формула Герона, позволяющая вычислить площадь треугольника, зная длины его сторон.

S= √ (p * (p - a)*(p - b)*(p - c)) ,где

S - площадь;
p - полупериметр треугольника (a+b+c)/2;
a,b,c - длины сторон треугольника.

Напишите программу, которая принимает на вход длины сторон треугольника и выводит его площадь
"""

import math
a, b, c = int(input('Введите сторону треугольника a: ')), int(input('Введите сторону треугольника b: ')), int(input('Введите сторону треугольника c: '))

p = (a + b + c) / 2
S = math.sqrt((p * (p - a)*(p - b)*(p - c)))

print('Площадь треугольника =', S)
