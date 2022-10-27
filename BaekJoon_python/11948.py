arr = [] 
for _ in range(6):  
    arr.append(int(input())) 
    
arr1 = sorted(arr[:4]) 
arr2 = arr[4:] 
print(sum(arr1[1:]) + max(arr2))