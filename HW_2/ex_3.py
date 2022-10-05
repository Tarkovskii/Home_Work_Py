number_n = int(input('Введите число n: '))
number_z = 0
rez_list = []

for i in range(1,number_n+1):
    number_z += int(((1+(1/i))**i))
    rez_list.append('{} : {}'.format (i,number_z)) 
print(rez_list)