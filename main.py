"""Задача 3. Приоритет задач
В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, а затем уже идут небольшие. Каждая из этих задач, по сути, просто огромный поток цифр. Ваша задача, как программиста этого центра, написать программу, которая поможет определять, какую из задач нужно решать в первую очередь. 
Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше всего цифр, и вывести на экран соответствующее сообщение. Если число отрицательное, то считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.
Пример работы программы:
Введите кол-во задач: 4
Введите число: 6
Введите число: 14
Введите число: 1
Введите число: 13434
Первая задача на обработку: 13434
"""
def numeral_count(num):
  count = 0
  while num > 0:
    num //= 10
    count += 1
  return count

how_numbers = int(input('Введите кол-во задач: '))
next_task  = 0
first_task = 0
for numbers in range(how_numbers):
  num = int(input('Введите число: '))
  task = numeral_count (num)
  if task > next_task:
    next_task = task
    first_task = num
print('Первая задача на обработку:', first_task)


  

