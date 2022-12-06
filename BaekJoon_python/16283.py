a, b, n, w = map(int, input().split())
answer = 0

aNum, bNum = 0, 0

for i in range(1, n) : 
    if a * i + b * (n - i) == w : 
        answer += 1
        aNum = i
        bNum = n - i

if answer == 1 : print(aNum, bNum)
else : print(-1)