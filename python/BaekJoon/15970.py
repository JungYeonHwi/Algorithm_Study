def distance(a):
    leng = 0 
    for i in range(len(a)):
        if i == 0 :
            leng += abs(a[i] - a[i + 1])
        elif i == len(a) - 1 : 
            leng += abs(a[i] - a[i - 1])
        else :
            leng += min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
    return leng

n = int(input())
answer = 0
arr = []

for i in range(n):
    loc, clr = map(int, input().split())
    arr.append([clr, loc]) 
arr.sort() 

num = arr[-1][0] 
for i in range(1, num+1) : 
    same = []
    for j in range(n) : 
        if arr[j][0] == i :
            same.append(arr[j][1])
    answer += distance(same)

print(answer)