cnt = int(input())
result = []

for i in range(cnt) : 
    n = int(input())
    price = list(map(int, input().split()))
    discount = []
    
    while len(discount) != n : 
        tmp = price.pop(0)
        if tmp // 0.75 in price : 
            discount.append(tmp)
            price.remove(tmp // 0.75)
    
    result.append(discount)
    
for i in range(len(result)) : 
    str = "Case #%d:"%(i+1)
    for r in result[i] : 
        str += " %d"%r

    print(str)