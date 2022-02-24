N = int(input())

for i in range(N) : 
    List = list(map(str, input().split()))
    num = float(List[0])
    answer = num
    
    for k in List[1:] : 
        if (k == '@') : answer *= 3
        elif (k == '%') : answer += 5
        elif (k == '#') : answer -= 7
    
    value = "{:.2f}".format(answer)
    print(value)