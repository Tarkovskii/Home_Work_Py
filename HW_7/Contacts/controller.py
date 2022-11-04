import user_i as us
import create_data as data
import create_file as cf
import find as fi


def do_it():
    us.menu()
    sav_dat = {}
    do = us.button_click()
    
    if do==3:
        exit()

    while do == 1:
        name = us.info_client_name()
        num = us.info_client_num()
        sav_dat = data.create_data(sav_dat,name, num)
        cf.create_txt(sav_dat)
        cf.creat_csv(sav_dat)

        do = int(input('Перейти к поиску - 2 '))



def do_ser():
    return fi.serch(us.serch_for_name(),fi.create_dict())