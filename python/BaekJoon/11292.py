while 1 :
    n = int(input())
    if n == 0 :
        break
    lst = []
    for i in range(n):
        name, L = input().split()
        L = float(L)
        lst.append([name, L])
    lst.sort(key= lambda x:-x[1])
    tmp = 0
    for name, L in lst :
        if L >= tmp :
            print(name, end=' ')
            tmp = L
    print()