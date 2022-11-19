a = int(input())
b = int(input())
arr = [a, b]

while 1 : 
    tmp = a - b
    if tmp > b : 
        arr.append(tmp)
        break
    else : 
        arr.append(tmp)
        a = b
        b = tmp
        
print(len(arr))