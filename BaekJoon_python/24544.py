N = int(input())
view = list(map(int,input().split()))
score = list(map(int,input().split()))

answer = 0

for i in range(N) :
    if score[i] == 0 : answer += view[i]

print(sum(view))
print(answer)