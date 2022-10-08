# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_nums = [1, 2, 3, 4, 6, 7, 8, 9]
list_res = []
size = len(list_nums)

if size % 2 != 0:
    size = size / 2 + 0.5
else:
    size /=2

size = round(size)

for i in range(0, size):
    sum = list_nums[i] * list_nums[len(list_nums)-i-1]
    list_res.append(sum)

print(list_nums)
print(list_res)