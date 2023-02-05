n = int(input())

arr = list(map(str, input().split()))

value = [i for i in range(1, n+1)]
check = 1

for a, b in zip(arr, value) : 
    
    if a == "mumble" : continue
    else : 
        if int(a) != b : check = 0
        
if check : print("makes sense")
else : print("something is fishy")