s = input()
v = input()

while v in s : 
    idx = s.index(v)
    s = s[:idx] + s[idx+len(v):]
    
if len(s) == 0 : print("FRULA")
else : print(s)