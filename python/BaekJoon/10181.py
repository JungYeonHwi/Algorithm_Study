while 1:
    n = int(input())
    if n == -1:
        break
    li = []
    for i in range(2, n//2+1):
        if n % i == 0:
            li.append(i)
    if sum(li) + 1 == n:
        print('{0} = 1 '.format(n), end = '')
        for j in li:
            print('+ {0} '.format(j) ,end = '')
    else:
        print('{0} is NOT perfect. '.format(n))