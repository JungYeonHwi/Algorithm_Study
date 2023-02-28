s = list(map(str, input()))
s.sort()

chk = ["I", "O", "S", "H", "Z", "X", "N"]

check = 1

for i in s : 
    if i not in chk : check = 0
    
if check : print("YES")
else : print("NO")