import math
import sys

n, kim, lim = map(int,sys.stdin.readline().split())
answer = 0

while 1 :
    if math.ceil(kim) == math.ceil(lim) : break
    kim = math.ceil(kim/2)
    lim = math.ceil(lim/2)
    answer +=1
 
print(answer)