# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

list_num = [1, 3, 4, 9, 8, 4, 6, 7, 8]
sum_pos = 0
list_odd_pos = []

for i in range(0, len(list_num)):
    if i % 2 != 0:
        list_odd_pos.append(list_num[i])
        sum_pos += list_num[i]

print(list_num)
print('{} -> {}'.format(list_odd_pos, sum_pos))