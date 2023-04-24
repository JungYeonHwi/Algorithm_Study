N = int(input())
 
time = [list(map(int, input().split())) for _ in range(N)]  
 
s = sorted(time, reverse=True)
e = sorted(time, key=lambda x:x[1]) 
 
if (s[0][0]-e[0][1]) < 0 : print(0)   
else : print(s[0][0]-e[0][1])