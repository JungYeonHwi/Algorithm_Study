n = int(input())
m = int(input())
mList = list(map(int, input().split()))
friends = [0 for _ in range(n)]

for i in range(m):
    target = mList[i]
    nList = list(map(int, input().split()))
    for j in range(n):
        if nList[j] == target : 
            friends[j] += 1
        else : 
            friends[target-1] += 1
for i in range(n) :
    print(friends[i])