import sys
hurtFinger = int(sys.stdin.readline())
maxRepeat = int(sys.stdin.readline())
answer = 0
hurtCount = 0

if hurtFinger == 1:
    if maxRepeat == 0:
        answer += hurtFinger - 1
    else :
        answer += 8 * maxRepeat
elif hurtFinger == 5 : 
    if maxRepeat == 0 : answer += hurtFinger - 1
    else : answer += 4 + 8 * maxRepeat
else :
    if maxRepeat == 0 : answer += hurtFinger - 1
    else : 
        answer += 4 * maxRepeat + 1
        if maxRepeat % 2 == 0 : answer += hurtFinger - 2
        else : answer += 4 - hurtFinger


print(answer)