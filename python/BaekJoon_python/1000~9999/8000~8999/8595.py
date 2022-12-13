n = int(input())
List = list(input())
d = '0123456789'
num = ''

for i in List : 
    if i in d : num += i
    else : num += ' '
    
print(sum(list(map(int, num.split()))))