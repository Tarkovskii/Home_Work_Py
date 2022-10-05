n = int(input('Введите число: '))
res = 1

for i in range(1,n+1):
    res *= i
    print(res, end=' ')

