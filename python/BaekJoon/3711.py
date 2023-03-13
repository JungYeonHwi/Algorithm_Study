for _ in range(int(input())):
    n = int(input())
    numbers = [int(input()) for i in range(n)]
    result = 0
    while 1 :
        result += 1
        if len({i % result for i in numbers}) == n :
            print(result)
            break