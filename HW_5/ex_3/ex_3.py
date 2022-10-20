# 3. Создайте программу для игры в ""Крестики-нолики"".

x = {'a1': '-', 'a2': '_', 'a3': '-',
     'b1': '_', 'b2': '-', 'b3': '_',
     'c1': '_', 'c2': '-', 'c3': '_'}

count = 0


print('  1 2 3')
print(f'A {x["a1"]} {x["a2"]} {x["a3"]}')
print(f'B {x["b1"]} {x["b2"]} {x["b3"]}')
print(f'C {x["c1"]} {x["c2"]} {x["c3"]}')


while count < 9:
    a = input('Введите позицию ')

    def hcange_pos(x, a):
        x[a] = 'x'

    res = hcange_pos(x, a)

    print('  1 2 3')
    print(f'A {x["a1"]} {x["a2"]} {x["a3"]}')
    print(f'B {x["b1"]} {x["b2"]} {x["b3"]}')
    print(f'C {x["c1"]} {x["c2"]} {x["c3"]}')

    def winner(x):
        if x['a1'] == x['a2'] and x['a2'] == x['a3']:
            print(f'Победили {x["a1"]}')
            return 9
        elif x['b1'] == x['b2'] and x['b2'] == x['b3']:
            print(f'Победили {x["b1"]} ')
            return 9
        elif x['c1'] == x['c2'] and x['c2'] == x['c3']:
            print(f'Победили {x["c1"]} ')
            return 9
        elif x['a1'] == x['b1'] and x['b1'] == x['c1']:
            print(f'Победили {x["a1"]} ')
            return 9
        elif x['a2'] == x['b2'] and x['b2'] == x['c2']:
            print(f'Победили {x["a2"]}')
            return 9
        elif x['a3'] == x['b3'] and x['b3'] == x['c3']:
            print(f'Победили {x["a3"]}')
            return 9
        elif x['a1'] == x['b2'] and x['b2'] == x['c3']:
            print(f'Победили {x["a1"]}')
            return 9
        elif x['a3'] == x['b2'] and x['b2'] == x['c1']:
            print(f'Победили {x["a3"]}')
            return 9

    res_win = winner(x)
    if res_win == 9:
        break

    count += 1
    if count == 9:
        print("Ничья")
        break

    b = input('Введите позицию ')

    def hcange_pos(x, b):
        x[b] = 'o'

    res = hcange_pos(x, b)
    print('  1 2 3')
    print(f'A {x["a1"]} {x["a2"]} {x["a3"]}')
    print(f'B {x["b1"]} {x["b2"]} {x["b3"]}')
    print(f'C {x["c1"]} {x["c2"]} {x["c3"]}')

    def winner(x):
        if x['a1'] == x['a2'] and x['a2'] == x['a3']:
            print(f'Победили {x["a1"]} ')
            return 9
        elif x['b1'] == x['b2'] and x['b2'] == x['b3']:
            print(f'Победили {x["b1"]} ')
            return 9
        elif x['c1'] == x['c2'] and x['c2'] == x['c3']:
            print(f'Победили {x["c1"]} ')
            return 9
        elif x['a1'] == x['b1'] and x['b1'] == x['c1']:
            print(f'Победили {x["a1"]} ')
            return 9
        elif x['a2'] == x['b2'] and x['b2'] == x['c2']:
            print(f'Победили {x["a2"]} ')
            return 9
        elif x['a3'] == x['b3'] and x['b3'] == x['c3']:
            print(f'Победили {x["a3"]} ')
            return 9
        elif x['a1'] == x['b2'] and x['b2'] == x['c3']:
            print(f'Победили {x["a1"]} ')
            return 9
        elif x['a3'] == x['b2'] and x['b2'] == x['c1']:
            print(f'Победили {x["a3"]} ')
            return 9

    count+=1
    res_win = winner(x)
    if res_win == 9:
        break