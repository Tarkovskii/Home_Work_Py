# 3. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

list_value = input('Введите числа через пробел: ').split(' ')
res_list = []

for e in list_value:
    count = list_value.count(e)
    if count < 2:
        res_list.append(e)
        
print(res_list)
