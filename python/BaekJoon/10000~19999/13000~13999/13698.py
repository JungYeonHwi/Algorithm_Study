s = input()
arr = [1, 2, 3, 4]
for c in s:
    if c == 'A' : arr[0], arr[1] = arr[1], arr[0]
    elif c == 'B' : arr[0], arr[2] = arr[2], arr[0]
    elif c == 'C' : arr[0], arr[3] = arr[3], arr[0]
    elif c == 'D' : arr[1], arr[2] = arr[2], arr[1]
    elif c == 'E' : arr[1], arr[3] = arr[3], arr[1]
    elif c == 'F' : arr[2], arr[3] = arr[3], arr[2]
    
print(arr.index(1)+1)
print(arr.index(4)+1)