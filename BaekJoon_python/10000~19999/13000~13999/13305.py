n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
m = price[0]

for i in range(n - 1) : 
    if price[i] < m : 
        m = price[i]
    
    res += m * road[i]
    
print(res)