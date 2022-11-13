import string

s = input()
check = input()
result = ''

arr = string.ascii_letters

for i in s : 
    if i in arr : 
        result += i
    

if check in result : print(1)
else : print(0)