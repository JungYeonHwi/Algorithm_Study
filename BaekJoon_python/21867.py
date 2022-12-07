import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

stack = []

for i in arr : 
    if i != "J" and i != "A" and i != "V" : stack.append(i)
    
if len(stack) == 0 : print("nojava")
else : print("".join(stack))