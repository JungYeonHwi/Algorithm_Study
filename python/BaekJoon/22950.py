import sys
import math
input = sys.stdin.readline()

N = int(input())
M = int(input())
K = int(input())

if "1" not in M : 
    print("YES")
    exit(0)
    
if K == 0 : 
    print("YES")
    exit(0)

count = 0

for i in range(len(M) - 1, -1, -1) : 
    if M[i] == "1" : 
        break
    if M[i] == "0" : count += 1
    
if count >= K : print("YES")
else : print("NO")