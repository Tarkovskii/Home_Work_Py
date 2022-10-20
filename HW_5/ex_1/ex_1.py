# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

patch = 'C:\\Users\\David\\Desktop\\Less_py\\home_work_py\\home_work\\HW_5\\any_txt.txt'
f = open(patch, 'r', -1, 'utf-8')
list_for_tx = []
x = 0
chars = 'абв'

for e in f:
    e = str(e.strip())
    e = e.lower()
    a=e.find('а') !=-1
    b=e.find('б') !=-1
    c=e.find('в') !=-1
    if a !=True and b !=True and c !=True:
        list_for_tx.append(e)  


f.close()


print(list_for_tx)