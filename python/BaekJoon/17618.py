n = int(input())
res = 0
for number in range(1, n+1):
    tmp = str(number)
    ds = 0
    
    for i in tmp :
        ds += int(i)
    if number % ds == 0:
        res += 1
print(res)