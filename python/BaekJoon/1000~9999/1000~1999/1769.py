def s(string, cnt) : 
    if len(string) > 1 : 
        cnt += 1
        t = 0
        for i in string :
            t += int(i)
        s(str(t), cnt)
        
    else : 
        if int(string) % 3 == 0 : 
            print(cnt)
            print("YES")
        else : 
            print(cnt)
            print("NO")

n = input()
cnt = 0
s(n, cnt)