import module as md
import view as ui


def do_it():
    command = 0
    while command < 9:
        ui.menu()
        command = int(input('Введите команду__'))
        if command == 1:
            employees = md.read_csv()
            while command == 1:
                md.serch_employee_for_id(employees)
                command = ui.go_out()
        elif command == 2:
            employees = md.read_csv()
            while command == 2:
                md.select_employee_for_position(employees)
                command = ui.go_out()
        elif command == 3:
            employees = md.read_csv()
            while command == 3:
                md.select_employee_for_salary(employees)
                command = ui.go_out()
        elif command == 4:            
            while command ==4:  
                employees = md.read_csv()              
                new_list = md.del_employee(employees)
                md.write_csv(new_list)
                command = ui.go_out()
        elif command == 5:
            while command == 5:
                new_employee = md.add_new_employee()
                md.add_wr_csv(new_employee)
                command = ui.go_out()
        elif command == 6:
            employees = md.read_csv()
            while command ==6:
                update_employees = md.update_data_employee(employees)
                md.write_csv(update_employees)
                command = ui.go_out()
        elif command == 7:
            employees = md.read_csv()
            md.write_json(employees)
            command = ui.go_out()
