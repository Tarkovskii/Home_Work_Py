# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))


def get_simple_mult(num):
    b = 2
    list_simple_value = []
    while num > 1:
        if num % b == 0:
            num = num/b
            list_simple_value.append(b)
            b = 2
        else:
            b += 1
    return list_simple_value


list_res = get_simple_mult(num)
print(list_res)