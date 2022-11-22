L, R = map(int, input().split())
l = R - L + 1
arr = []

for i in range(L, R+1) : 
    num = list(str(i))
    cnt = num.count("8")
    arr.append(cnt)
    
print(min(arr))