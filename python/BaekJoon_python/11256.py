for _ in range(int(input())) : 
    j, n = map(int, input().split())
    box = []
    for i in range(n) : 
        a, b = map(int, input().split())
        box.append(a*b)
    box.sort(reverse=True)
    answer = 0
    
    for i in box : 
        j -= i
        answer += 1
        if j <= 0 : 
            print(answer)
            break