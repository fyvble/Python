"""Задача 2. Таблица суммы
Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N."""



for row in range (20):
  for col in range(50):
    if col  == 24:
      print('|', end = '')
    elif row  == 9:
      print('-', end = '')
    else:
      print(' ', end = '')
    
  print()
  