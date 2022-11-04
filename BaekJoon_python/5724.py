while 1 :
    n = int(input())
    if n == 0 : break
    answer = 0
    for i in range(1, n+1) : answer += (n - i + 1) ** 2
    print(answer)