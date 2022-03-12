import sys

n = int(sys.stdin.readline())
List = []

for _ in range(n) : 
    List.append(int(sys.stdin.readline()))

List.sort()
answer = 0

for i in range(n-1):
    answer += List[i] + List[i+1]
    List[i+1] = answer
    
print(answer)