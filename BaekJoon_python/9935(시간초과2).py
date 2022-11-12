s = input()
v = input()

while v in s : 
    s = s.replace(v, "")
    
if len(s) == 0 : print("FRULA")
else : print(s)