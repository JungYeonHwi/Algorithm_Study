s = int(input())
s +=1
s = list(map(int,list(str(s))))

for i in range(10000) :
    for i in range(0,len(s)//2+1) :
        if s[i] < s[len(s)-i-1] :
            s[len(s)-i-2] += 1
        s[len(s)-i-1] = s[i]
        for i in range(len(s)-1, -1, -1) :
            if s[i] >= 10 :
                s[i], s[i-1] = s[i] % 10, s[i-1] + s[i] // 10

for i in s:
    print(i,end="")