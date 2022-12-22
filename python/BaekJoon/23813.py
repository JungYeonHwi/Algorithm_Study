arr = list(map(int, input()))
answer = 0

for i in range(len(arr)) : 
    value = arr.pop()
    arr.insert(0, value)
    result = int(''.join(str(x) for x in arr))
    
    answer += result
    
print(answer)