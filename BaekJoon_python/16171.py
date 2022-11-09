s = input()
check = input()
tmp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in s : 
    if i in tmp : 
        s = s.replace(i, "")
        
if check in s : print(1)
else : print(0)