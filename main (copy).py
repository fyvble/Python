bank = int(input('Сколько денег на счету? '))
if bank > 75000:
  bank -= 75000
  print('Курс успешно приобретён')
  if bank < 5000:
    print('Сделана скидка')
    bank += 1000
    print('Остаток на счету:', bank)
else:
  print('Не хватает денег на счету')
print('Хорошего дня!') 
