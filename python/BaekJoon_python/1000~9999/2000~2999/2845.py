L, P = map(int, input().split())

cnt = L * P

List = list(map(int, input().split()))

for i in List : 
    print(i-cnt, end=' ')