List = list(map(int, input().split()))
List.sort()

a = List[0]
b = List[1]
c = List[2]

word = input()
answer = []

for i in word : 
    if i == 'A' : answer.append(a)
    elif i == 'B' : answer.append(b)
    else : answer.append(c)

a = " ".join(map(str, answer))
print(a)