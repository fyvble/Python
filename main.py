"""Задача 2. Почта 2
На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.
Реализуйте функцию, которая получает все эти данные и выводит на экран. В программе вызовите функцию три раза с разными значениями аргументов.
Подсказка: семь аргументов.

"""
def pochta(first_name, name, country, city, street, house, flat):
  print()
  print('Фамилия:', first_name)
  print('Имя:', name)
  print('Страна:', country)
  print('Город:', city)
  print('Улица:', street)
  print('Дом:', house)
  print('Квартира:', flat)
  print()

for test in range(3):
  first_name = input('Введите фамилию: ')
  name = input('Введите имя: ')
  country = input('Введите страну: ')
  city = input('Введите город: ')
  street = input('Введите улицу: ')
  house = input('Введите номер дома: ')
  flat = input('Введите номер квартиры: ')
 
pochta(first_name, name, country, city, street, house, flat)
  