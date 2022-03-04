n = int(input())
List = []

for _ in range(n) : 
    List.append(input())

s = set(List)
answer = list(s)

answer.sort()
answer.sort(key = len)

for i in answer : 
    print(i)