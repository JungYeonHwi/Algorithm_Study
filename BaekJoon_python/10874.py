import sys

for _ in range(int(sys.stdin.readline())) :
    
    List = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    
    for i in range(10) :
        if List[i] == (i+1)%5 : cnt+=1
        
    if cnt == 8 : print(_+1)