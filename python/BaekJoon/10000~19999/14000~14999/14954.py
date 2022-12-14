def change(a) :
    s = 0
    while a//1 != 0 :
        s += (a%10)**2
        a = int(a/10)
    return s

n = int(input())

while 1 :
    n = change(n)
    if n == 4 :
        print('UNHAPPY')
        break
    elif n == 1 :
        print('HAPPY')
        break