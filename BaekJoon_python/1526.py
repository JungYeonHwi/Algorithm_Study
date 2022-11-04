n = int(input())

while 1 :
    flag = 1
    for i in str(n) :
        if i != '4' and i != '7' :
            flag = 0
            n -= 1
    if flag :
        print(n)
        break