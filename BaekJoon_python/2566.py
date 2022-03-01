num = 0

for i in range(9) : 
    row = list(map(int, input().split()))
    
    if (max(row) > num) : 
        num = max(row)
        x = i + 1
        y = row.index(num) + 1
        
print(num)
print(x, y)