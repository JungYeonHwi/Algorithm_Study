n = int(input())
nums = list(map(int, input().split()))

odds = 0
evens = 0

for i in nums :
    if i % 2 == 0 :
        evens += 1
    else :
        odds += 1
if n % 2 == 1 :
    if odds == n // 2 + 1 and evens == n // 2 :
        print(1)
    else : print(0)
else :
    if odds == n // 2 and evens == n // 2 :
        print(1)
    else : print(0)