def digit(n) :
    ans = 1
    for i in str (n) :
        ans *= int(i)
    return ans
 
n = input()
cnt = 0

while int (n) >= 10 :
    if int(n) < 10 : break
    n = digit(n)
    cnt += 1
print(cnt)