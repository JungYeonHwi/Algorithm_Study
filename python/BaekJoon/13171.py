a = int(input())
x = int(input())
ans = 1
xtobin = bin(x)[2:][::-1]
tmp = []
for i in range(65) :
    tmp.append(a)
    a = a**2
    a %= 1000000007
for i in range(len(xtobin)) :
    if int(xtobin[i]) == 1 :
        ans *= tmp[i]
        ans %= 1000000007
print(ans)