s = input()
a = 0; b = 0;

for i in range(len(s)) : 
    if s[i] == "A" : a = a + int(s[i+1])
    elif s[i] == "B" : b = b + int(s[i+1])

if a > b : print("A")
else : print("B")