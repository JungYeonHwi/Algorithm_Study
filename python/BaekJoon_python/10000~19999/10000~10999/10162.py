N = int(input())
ACount = 0
BCount = 0
CCount = 0

if (N % 10 != 0) : print("-1")
else : 
    ACount = N // 300
    N %= 300
    BCount = N // 60
    N %= 60
    CCount = N // 10
    N %= 10

    print(ACount, BCount, CCount)