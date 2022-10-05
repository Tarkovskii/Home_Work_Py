num = int(input('Введите число n: '))
found_pos_first = input('Введите номер первой позиции: ')
found_pos_sec = input('Введите номер второй позиции: ')


def create_list(num):
    list_pos = []
    for i in range(-num, num+1):
        list_pos.append(i)
    return list_pos


def create_file(n, list_pos,):
    pos_file = open('file.txt', 'w')
    for n in range(0, len(list_pos)):
        n_str = str(n)
        pos_file.writelines('{}\n'.format(n_str))
    return pos_file


pos_file = open('file.txt', 'r')

for check_pos in pos_file:
    if check_pos.__contains__(found_pos_first):
        int_check_first = int(check_pos)
        
pos_file = open('file.txt', 'r')
    
for check_pos in pos_file:
    if check_pos.__contains__(found_pos_sec):
        int_check_sec = int(check_pos)


list_pos = create_list(num)
pos_file = create_file(num, list_pos)
res = (list_pos[int_check_first] + list_pos[int_check_sec]) / 2

print(list_pos)
print(list_pos[int_check_first])
print(list_pos[int_check_sec])

print('Среднее арифметическое {} и {} = {}'.format(
    list_pos[int_check_first], list_pos[int_check_sec], res))

pos_file.close()
