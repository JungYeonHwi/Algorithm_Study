import sys
input = sys.stdin.readline

n, m = map(int,input().split())
List = list(map(int,input().split()))

for i in range(n-1) :
    List[i+1] += List[i]
List = [0] + List

for _ in range(m) : 
    a, b = map(int,input().split())
    print(List[b] - List[a-1])