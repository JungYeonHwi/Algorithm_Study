def distance(a):
    leng = 0 
    for i in range(len(a)):
        if i == 0 : 
            leng += abs(a[i] - a[i + 1])
        elif i == len(a) - 1 : 
            leng += abs(a[i] - a[i - 1])
        else : 
            leng += min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
    return leng

n = int(input())
answer = 0
swp = []

for i in range(n):
    loc, clr = map(int, input().split())
    swp.append([clr, loc])
swp.sort()

clr = swp[-1][0] 
for i in range(1,clr+1) : 
    same_clr = [] 
    for j in range(n) : 
        if swp[j][0] == i :
            same_clr.append(swp[j][1])
    answer += distance(same_clr)

print(answer)