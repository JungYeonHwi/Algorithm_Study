l = int(input())
d = int(input())
x = int(input())

arr = []

for i in range(l, d+1) : 
    value = list(map(int, str(i)))
    if x == sum(value) : arr.append(i)
    
print(min(arr))
print(max(arr))