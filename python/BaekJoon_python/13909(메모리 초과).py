n = int(input())
arr = ["0" for _ in range(n+1)]

for i in range(1, n+1) : 
    for idx in range(0, n+1, i) : 
        if arr[idx] == "0" : arr[idx] = "1"
        else : arr[idx] = "0"
        
answer = arr[1:].count("1")
print(answer)