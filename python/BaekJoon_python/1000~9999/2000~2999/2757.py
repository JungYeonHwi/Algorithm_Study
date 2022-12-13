from string import ascii_uppercase

while 1 : 
    arr = input()
    s = arr[1:]
    r, c = map(int,s.split('C'))
    if r == 0 and c ==0 : break
    else :
        c -= 1
        alpha = list(ascii_uppercase)
        lst = []
        while c >= 0 :
            d = c % 26
            c = c // 26 -1
            lst.insert(0, d)
            
        ans =''
        for x in lst : ans += alpha[x]

        ans += str(r)
        print(ans)