s = list(input())
t = list(input())

answer = 0

while t : 
    if t[-1] == 'A' : t.pop()
    elif t[-1] == 'B' : 
        t.pop()
        t.reverse()
    if s == t : 
        answer = 1
        break
    
if answer : print(1)
else : print(0)