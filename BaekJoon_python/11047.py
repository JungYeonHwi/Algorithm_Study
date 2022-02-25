N, K = map(int, input().split())
List = []

for i in range(N) : 
    n = int(input())
    List.append(n)
    
List.sort(reverse=True)
c = 0

for i in List : 
    c += K // i
    K %= i

print(c)