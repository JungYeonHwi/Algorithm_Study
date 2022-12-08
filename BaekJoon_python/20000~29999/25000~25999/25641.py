n = int(input())
s = input()

while 1 : 
    sCnt = s.count("s")
    tCnt = s.count("t")
    
    if sCnt <= 0 or tCnt == 0 : break
    else : 
        if sCnt == tCnt : break
        else : 
            s = s[1:]
            
print(s)