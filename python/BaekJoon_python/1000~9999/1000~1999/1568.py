n = int(input())
k = 0
time = 0

while (1) : 
    k += 1
    
    if (n == 0) : break
    if (n <k) : k = 1
    n -= k
    time += 1
    
print(time)