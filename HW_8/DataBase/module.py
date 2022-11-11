import csv
import json


def read_csv() -> list:
    employee = []
    with open('base.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp['id'] = int((row[0]))
            temp['last_name'] = row[1]
            temp['first_name'] = row[2]
            temp['position'] = row[3]
            temp['numb'] = row[4]
            temp['salary'] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    with open('base.json', 'r', encoding='utf-8') as fin:
        temp = json.load(fin)
    return temp


def write_csv(employees: list):
    with open('base.csv', 'w',newline='', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open('base.json', 'w', encoding='utf-8') as fout:
        fout.write(json.dumps(employees, indent=2) + '\n')


def serch_employee_for_id(employees: list):
    id = int(input('Введите "id" сотрудника, которого хотите найти__'))
    for employee in employees:
        if employee['id'] == id:
            print(employee)


def select_employee_for_position(employees: list):
    for employee in employees:
        print(f'{employee["first_name"]} - {employee["position"]}')


def select_employee_for_salary(employees: list):
    for employee in employees:
        print(f'{employee["first_name"]} - {employee["salary"]}')


def add_new_employee():
    list = []
    temp = {}
    temp['id'] = int(input('add id for employee '))
    temp['last_name'] = input('input firstname ')
    temp['first_name'] = input('input lastname ')
    temp['position'] = input('input position ')
    temp['numb'] = input('input nnmber ')
    temp['salary'] = float(input('input salary for employees '))
    list.append(temp)
    return list


def add_wr_csv(employee: list):
    with open('base.csv', 'a', encoding='utf-8') as f:
        for i, k in employee[0].items():
            f.writelines(f'{k},')
        f.write('\n')


def overwrite_csv(employee: list):
    with open('base.csv', 'w', encoding='utf-8') as f:
        try:
            for i, k in employee[0].items():
                f.writelines(f'{k},')
            f.write('\n')
        except IndexError:
            print('Список сотрудников пуст__')


def update_data_employee(employees: list):
    id = int(input('Введите "id" сотрудника, данные которого хотите обновить.__'))
    parametr = input('Какие данные хотите обновить?__')
    change = input('Введите новые данные___')
    update_dic = {}
    update_employees = []
    for employee in employees:
        if employee['id'] == id:
            for k, v in employee.items():
                if k == parametr:
                    update_dic[k] = change
                else:
                    update_dic[k] = v
            update_employees.append(update_dic)
        else:
            update_employees.append(employee)

    return update_employees


def del_employee(employees: list):
    id = int(input('Введите "id" сотрудника, которого хотите удалить__'))
    nem_list_employees = []
    for employee in employees:
        if employee['id'] != id:
            nem_list_employees.append(employee)
    return nem_list_employees
