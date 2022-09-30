ax = int(input('Введите точку x1: '))
ay = int(input('Введите точку y1: '))
bx = int(input('Введите точку x2: '))
by = int(input('Введите точку y2: '))

ab_size = (((bx-ax)**2)+((by-ay)**2))**(0.5)

print('{0:.2f}'.format((ab_size)))