n = int(input())

i = 2

cnt = 1
while i * i <= n : 
    if n % i == 0 : 
        cnt = n // i
        break
    
    i += 1
    
print(n - cnt)