T = int(input())
 
for _ in range(T) :
    s = input().replace(' ', '')
    c = [0] * 26
 
    for i in s :
        c[ord(i) - 97] += 1
 
    if c.count(max(c)) > 1 : print('?')
    else : print(chr(97 + c.index(max(c))))
