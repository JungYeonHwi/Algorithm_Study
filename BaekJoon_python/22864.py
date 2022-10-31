A, B, C, M = map(int, input().split())

whole = 24
fatigue = 0
answer = 0

if A > M : answer = 0
else : 
    for i in range(1, 25) :
        if fatigue + A <= M:
            fatigue += A
            answer += B
        else:
            fatigue -= C
            if fatigue < 0:
                fatigue = 0
print(answer)