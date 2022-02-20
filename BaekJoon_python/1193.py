N = int(input())

line = 0
maxNum = 0

while N > maxNum : 
    line += 1
    maxNum += line

gap = maxNum - N 
if line % 2 == 0 :
    top = line - gap
    under = gap + 1
else :
    top = gap + 1 
    under = line - gap 

print(f'{top}/{under}')