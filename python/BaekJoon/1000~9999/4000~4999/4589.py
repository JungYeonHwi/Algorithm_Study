n = int(input())

print("Gnomes:")

for _ in range(n) : 
    arr = list(map(int, input().split()))
    copy = list(arr)
    checkArr1 = list(arr)
    checkArr2 = list(arr)
    checkArr1.sort()
    checkArr2.sort(reverse=True)
    
    check1 = 0
    check2 = 0
    
    if copy != checkArr1 and copy != checkArr2 : print("Unordered")
    else : print("Ordered")