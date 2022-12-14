n = int(input())
arr = []
 
for _ in range(n) :
    arr.append(input())
 
 
if sorted(arr) == arr : print("INCREASING")
elif sorted(arr, reverse= True) == arr : print("DECREASING")
else : print("NEITHER")