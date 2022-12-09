import sys
input = sys.stdin.readline

def g(a, b) :
    if b == 0 : return a
    else : return g(b, a%b)

def lcm(a,b) :
    return a*b // g(a,b)

a, b = map(int,input().split())

print(lcm(a,b))