h = input()
n = input()
cnt = 0
while 1 : 
    if n not in h : 
        break
    else : 
        cnt += 1
        h = h.replace(n, "", 1)
        
print(cnt)