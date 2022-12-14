n = int(input())
arr = list(map(int, input().split()))
arr.sort()

check = list(input())
value = []

for i in check : 
    if i == " " : value.append(0)
    elif i.isupper() : value.append(ord(i)-64)
    elif i.islower() : value.append(ord(i)-70)
    
value.sort()

if value == arr : print("y")
else : print("n")