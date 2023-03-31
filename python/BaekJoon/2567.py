N = int(input())
arr=[[False for _ in range(101)] for _ in range(101)] 
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(x,x+10): 
        for j in range(y,y+10):
            arr[j][i] = True 

total=0  
dx=[0,0,1,-1] 
dy=[1,-1,0,0]
for i in range(101):   
    for j in range(101):
        if arr[j][i] == True: 
            tmp=0
            for k in range(4):
                if arr[j+dy[k]][i+dx[k]] == True:
                    tmp+=1
        
            if tmp == 3:  
                total +=1
            elif tmp == 2:
                total +=2

print(total)