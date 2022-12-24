n = int(input())
nList = list(map(int, input().split()))
ans = 0
cnt = 0
menu = [False] * 111111

for num in nList :
    if not menu[num] : 
        cnt += 1
        menu[num] = True
    else :
        cnt -= 1
        menu[num] = False

    ans = max(ans, cnt)

print(ans)