check = ["pi", "ka", "chu"]

s = input()

for i in check :
    if i in s : s = s.replace(i, "*")
    
flag = True

for i in s : 
    if i != "*" : flag = False

if flag : print("YES")
else : print("NO")