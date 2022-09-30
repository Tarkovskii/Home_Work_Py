x = int(input('Ведите координату х: '))
y = int(input('Введите координату у: '))

if x>0 and y>0:
    print(f'x = {x}, y = {y} -> 1')
elif x<0 and y>0:
    print(f'x = {x}, y = {y} -> 2')
elif x<0 and y <0:
    print(f'x = {x}, y = {y} -> 3')
elif x>0 and y <0:
    print(f'x = {x}, y = {y} -> 4')
else:
    print('Введите другие координаты')