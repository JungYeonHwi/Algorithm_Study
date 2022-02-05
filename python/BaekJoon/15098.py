s = input().split(' ')
arr = {}
answer = True
for i in s :
    if i not in arr.keys() :
        arr[i] = 1
    else :
        arr[i]+=1

for i in arr.values() :
    if i != 1 :
        answer = False
        break
if answer == False :
    print('no')
else :
    print('yes')