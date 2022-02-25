N = int(input())
Acount = BCount = CCount = 0

if (N < 10) : print(-1)
elif (N % 10 == 0 and N < 60) : CCount += (N // 10)

print(Acount, BCount, CCount)