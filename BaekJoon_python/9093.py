t = int(input())

for _ in range(t) : 
    List = list(map(str, input().split(' ')))
    s = ''
    
    for idx in List : 
        temp = idx[::-1]
        s += temp + ' '
    print(s)