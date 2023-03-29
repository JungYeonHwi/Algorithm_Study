from sys import stdin

t = int(stdin.readline())

for i in range(t) : 
    arr = list(map(int, stdin.readline().split(" ")))
    ml = max(arr)
    
    shortest = (sum(arr) - ml) ** 2 + ml ** 2
    print(shortest)