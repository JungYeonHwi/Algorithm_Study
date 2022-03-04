N = int(input())
List = list(map(int, input().split()))

seat = [0] * 100
cnt = 0

for i in List : 
    if seat[i-1] == 0 : seat[i-1] = 1
    else : cnt += 1
    
print(cnt)