# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

num_k = int(input('Введите значение натуральной степени: '))

def create_srt(num_k):
    num_first = random.randint(0,100)
    num_sec = random.randint(0,100)
    if num_k <=1:
        srt = '{}*x + {}*x = 0'.format(num_first,num_sec)
        return srt
    else:
        srt = '{}*x^{} + {}*x = 0'.format(num_first,num_k,num_sec)
        return srt


def create_file(str):
    data = open('file_val.txt', 'w')
    index = 0
    found_symb = result.find('*')

    while index < found_symb:
        data.write(result[index])
        index +=1
    data.close()

result = create_srt(num_k)
data = create_file(result)
print(result)