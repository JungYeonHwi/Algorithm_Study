n = int(input())

List = list(map(int, input().split()))
    
List.sort()
answer = []
num = 0

for i in List :
    num += i
    answer.append(num)
print(sum(answer))