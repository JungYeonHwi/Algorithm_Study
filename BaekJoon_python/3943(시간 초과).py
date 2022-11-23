import sys
for _ in range(int(sys.stdin.readline())) :
    tmp = []
    n = int(sys.stdin.readline())
    while 1 :
        if 1 in tmp : break
        
        tmp.append(n)
        
        if n % 2 == 0 : n //= 2
        else : n = n * 3 + 1
    print(max(tmp))