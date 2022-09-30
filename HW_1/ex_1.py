number_day = int(input('Введите номер дня недели: '))

if number_day == 6 or number_day == 7:
    print('Выходной')
elif number_day <= 5 and number_day>0:
    print('Не выходной')
else:
    print('Введите число от 1 до 7')