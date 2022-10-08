# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите n: '))


def create_list_neg_fib(n):
    f_1 = 1
    f_2 = -1
    list_nf = [f_1, f_2]
    for i in range(2, n):
        f_1, f_2 = f_2, f_1-f_2
        list_nf.append(f_2)
    list_nf.reverse()
    return list_nf


def create_list_fib(n):
    f1 = 0
    f2 = 1
    list_f = [f1, f2]
    for i in range(2, n+1):
        f1, f2 = f2, f1+f2
        list_f.append(f2)
    return list_f


def create_res_list(list_nf, list_f):
    for i in list_f:
        list_nf.append(i)
    return list_nf


list_neg_fib = create_list_neg_fib(n)
list_fib = create_list_fib(n)
list_res = create_res_list(list_neg_fib, list_fib)

print(list_res)
