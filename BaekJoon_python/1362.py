cnt = 0
while 1 :
    o, w = map(int, input().split())
    if o == 0 and w == 0 :
        quit()

    die = False
    while 1 :
        action, n = input().split()
        if action == '#' and n == '0' :
            break

        if not die :
            n = int(n)
            if action == 'E' :
                w -= int(n)
            elif action == 'F' : 
                w += int(n)

        if w <= 0 :
            die = True

    cnt += 1
    if w <= 0 :
        print("%d RIP" % cnt)
    elif o / 2 < w < o * 2 :
        print("%d :-)" % cnt)
    else :
        print("%d :-(" % cnt)