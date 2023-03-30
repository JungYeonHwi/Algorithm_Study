tc = int(input())
repeat = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]

for k in range(tc):
    num = int(input())
    key = num % 28
    change = "{0:b}".format(repeat[key]).zfill(4)
    for v in change:
        if v == '0':
            print('V', end='')
        else:
            print('딸기', end='')
    print("")