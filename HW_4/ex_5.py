# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

patch_fir = 'C:\\Users\\David\\Desktop\\Less_py\\file_val.txt'
patch_sec = 'C:\\Users\\David\\Desktop\\Less_py\\home_work_py\\home_work\\HW_4\\file_val_sec.txt'


def create_list_first(patch_fir):
    data = open(patch_fir, 'r')
    list_fir = []

    for e in data:
        list_fir.append(int(e))

    return list_fir


def create_list_sec(patch_sec):
    data = open(patch_sec, 'r')
    list_sec = []

    for e in data:
        list_sec.append(int(e))

    return list_sec


def create_result_file(list_a, list_b):
    data = open('file_res.txt', 'w')
    res_list = []

    for elem in list_a:
        res_list.append(elem)

    for elem in list_b:
        res_list.append(elem)

    res_list = sum(res_list)

    res_list = str(res_list)

    for i in res_list:
        data.write(i)

    data.close()
    
    return res_list


list_a = create_list_first(patch_fir)
list_b = create_list_sec(patch_sec)
list_c = create_result_file(list_a,list_b)
print(list_a)
print(list_b)
print(list_c)