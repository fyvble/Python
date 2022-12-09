"""Задача 2. Таблица суммы
Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N."""

for row in range(20):
  for col in range(50):
    if row == 9:
      print('-', end='')
    elif col == 24:
      print('|', end='')
    elif -row + 19 == col:
      print("/", end='')
   
    elif row + 29 == col:
      print("\\", end='')
    else:
      print(' ', end='')

  print()
