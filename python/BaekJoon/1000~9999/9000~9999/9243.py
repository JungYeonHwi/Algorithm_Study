N = int(input())
a, b = list(input()), list(input())

for _ in range(N) :
    for i in range(len(a)) :
        if a[i] == '0' :
            a[i] = '1'
        else :
            a[i] = '0'
            
if a == b : print("Deletion succeeded")
else : print("Deletion failed")