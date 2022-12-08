n = int(input())
arr = list(map(int,(input().split())))

temp = arr[0] ; s = 0
answer = []

for i in range(1,n):
    if arr[i] - temp >0 :
        s += arr[i]-temp
        temp = arr[i]
        
    elif arr[i] == temp or arr[i]-temp<0 :
        answer.append(s) 
        temp = arr[i] 
        s = 0
        
answer.append(s) 

if len(answer) == 0 : print(0) 
else : print(max(answer)) 