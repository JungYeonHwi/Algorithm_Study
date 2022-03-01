n = int(input())
List = list(map(int, input().split()))
c = 0

for i in List : 
    if (i == n) : c += 1
    
print(c)