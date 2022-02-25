T = int(input())

for i in range(T) : 
    a, b = map(int, input().split())
    count = 0
    
    for i in range(a, b+1):
        w = str(i)
        count += w.count('0')
        
    print(count)