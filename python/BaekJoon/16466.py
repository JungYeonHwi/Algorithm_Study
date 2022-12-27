import sys

N = int(sys.stdin.readline())
sold = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1) :
    if(sold[i-1] != i) :
        print(i)
        sys.exit()

print(N+1)