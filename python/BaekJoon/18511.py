from itertools import product

n, k = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(n))

while 1 :
    temp = list(product(arr, repeat=length))
    ex = []
    for i in temp :
        now = int(''.join(i))
        if now <= n : ex.append(now)
    if len(ex) >= 1 : 
        print(max(ex))
        break
    else :
        length -= 1