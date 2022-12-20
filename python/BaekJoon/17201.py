n = int(input())
s = input()
check = s[:2]
flag = 1
for i in range(2, n*2, 2) : 
    if s[i:i+2] != check : 
        flag = 0
        
if flag : print("Yes")
else : print("No")