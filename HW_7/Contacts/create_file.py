def create_txt(sav_data):
    list =[]
    for i in sav_data:
        list.append(f'{i}-{sav_data[i]}')

    with open('my_contacts.txt', 'a') as f:
        for i in list:
            i = str(i)
            f.write(f'{i}\n')

def creat_csv(sav_data):
    with open('my_contact.csv','w') as f:
        for k,v in sav_data.items():
            f.write(f'{k};{v}\n')