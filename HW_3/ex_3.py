# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list_nums = [1.1, 1.2, 3.1, 5, 10.01]


def create_nem_list(list_nums):
    list_new = []
    for pos in list_nums:
        b = round(((pos * 100) % 100), 1)
        if b > 0:
            list_new.append(b)
    return list_new


def get_max(list_res):
    max = list_res[0]
    for pos in list_res:
        if pos > max:
            max = int(pos)
    return max


def get_min(list_res):
    min = list_res[0]
    for pos in list_res:
        if pos < min:
            min = int(pos)
    return min


list_res = create_nem_list(list_nums)
max = get_max(list_res)
min = get_min(list_res)
res = max - min
print('{} -> {}'.format(list_nums, res))