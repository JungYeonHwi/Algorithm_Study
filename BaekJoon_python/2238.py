import sys
input = sys.stdin.readline

U, N = map(int, input().split())
p = [[] for _ in range(10001)]
num = [0 for _ in range(10001)]
m = 10001

for _ in range(N) :
    name, price = input().split()
    price = int(price)
    p[price].append(name)
    num[price] += 1
    
for i in range(10001) : 
    if num[i] != 0 : m = min(num[i], m)
    
for i in range(10001) : 
    if m == num[i] : 
        print(p[i][0],i)
        break