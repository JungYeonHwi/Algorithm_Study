import sys

d, k = map(int, sys.stdin.readline().rsplit())
first = [1,0]
second = [0,1]
p, q = 0, 0

for i in range(3, d+1):
    p = first[0] + second[0]
    q = first[1] + second[1]
    first = second[:]
    second = [p, q]

a = 1
while 1 :
    x = p * a
    y = k - x
    if y % q == 0:
        print(a)
        print(y//q)
        break

    a += 1