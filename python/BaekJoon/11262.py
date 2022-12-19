import decimal

for _ in range(int(input())) : 
    arr = list(map(int, input().split()))
    n = arr[0]
    del arr[0]
    
    avg = sum(arr) / n
    cnt = 0
    
    for i in arr : 
        if i > avg : cnt += 1
        
    print(f"{decimal.Decimal(avg):.3f} {decimal.Decimal(cnt/n * 100):.3f}%")