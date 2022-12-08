N = int(input())
List = list(map(int, input().split()))
v = int(input())

cnt = 0

for i in List : 
    if i == v : cnt += 1
    
print(cnt)