n, m = map(int, input().split())
six = []
one = []

for _ in range(m) : 
    s, o = map(int, input().split())
    six.append(s)
    one.append(o)
    
sm = min(six)
om = min(one)

if sm <= om * 6 : 
    answer = sm * (n // 6) + om * (n % 6)
    if sm < om * (n % 6) : answer = sm * (n // 6 + 1)
else : answer = om * n

print(answer)