N, I = map(int, input().split(" "))

arr = []

for i in range(N) : 
    s = input()
    arr.append(s)
    
arr.sort()

print(arr[I-1])