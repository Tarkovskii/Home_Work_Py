import user_i as us


def create_dict():
    empty_str = []
    cont_form_dic = {}

    with open('my_contacts.txt', 'r') as data:

        for line in data:
            empty_str.append(f'{line}')

    for i in range(0, len(empty_str)):
        now_srt = str(empty_str[i])
        ch_separator = now_srt.index('-')

        if now_srt[:ch_separator] in cont_form_dic:
            cont_form_dic[now_srt[:ch_separator]].append(
                now_srt[ch_separator+1:])
        else:
            cont_form_dic[now_srt[:ch_separator]] = [now_srt[ch_separator+1:]]

    return cont_form_dic


def serch(name_ser, data):
    a = 0
    while a == 0:
        try:
            data[name_ser]
        except KeyError:
            print(f'{name_ser} - не найденно.\n')
            name_ser = input(
                'Введите корректные данные.\nВыйти, нажмите - 3\n')
            if name_ser == '3':
                break
        else:
            a += 1
            row = ' '
            for cont in data[name_ser]:
                for ch in cont:
                    if ch == '\n':
                        ch = '  '
                        row += ch
                    else:
                        row += ch

            print(f'Номер {name_ser} - {row}')