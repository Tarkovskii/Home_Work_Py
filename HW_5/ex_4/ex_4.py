# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

f = open('file_for_corection.txt', 'w')
data_for_file = 'tteest teesstt ttteeesssttt'
f.write(data_for_file)
f.close()


def rle_encode(data):
    data = open('file_for_corection.txt', 'r')
    prev_i = ''
    rle = ''
    count = 1

    for line in data:
        for i in line:
            if i != prev_i:
                if prev_i:
                    rle += f'{str(count)}{prev_i}'
                prev_i = i
                count = 1
            else:
                count += 1
        else:
            rle += str(count) + i
            return rle
    data.close()


def create_file_rle(x):
    data = open('res_erl_file.txt', 'w')
    data.write(x)
    data.close()


def get_decod_file():
    data = open('res_erl_file.txt', 'r')
    f_decod = open('file_decod.txt', 'w')

    str_txt = ''

    for line in data:
        for char in line:
            str_txt += char

    res_srt = ''

    for i in range(0, len(str_txt)):
        if i % 2 == 0:
            a = int(str_txt[i])
        else:
            res = str(a*str_txt[i])
            res_srt += res
    data.close()
    return f_decod.write(res_srt)


res = rle_encode(f)

create_file_rle(res)

get_decod_file()

f.close()