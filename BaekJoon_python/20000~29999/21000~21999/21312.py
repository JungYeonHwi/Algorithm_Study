arr = list(map(int,input().split()))
odd = []

for i in range(3) :
    if (arr[i] %2) != 0 :
        odd.append(arr[i])
ans = 1

if not odd :
    for i in range(3) : ans *= arr[i]
else :
    for i in range(len(odd)) : ans *= odd[i]
print(ans)