import sys

input = sys.stdin.readline

dictionary = dict()

n, m = map(int, input().split())

for i in range(1, n+1) : 
    name = input().rstrip()
    dictionary[i] = name
    dictionary[name] = i

for i in range(m) :
    quest = input().rstrip()
    
    if quest.isdigit() : print(dictionary[int(quest)])
    else : print(dictionary[quest])