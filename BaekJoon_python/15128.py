p1, q1, p2, q2 = map(int, input().split())
answer = p1 / q1 * p2 / q2 / 2
if int(answer) == answer : print(1)
else : print(0)