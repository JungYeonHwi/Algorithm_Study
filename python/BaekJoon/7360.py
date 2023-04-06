import sys

while 1:
    plays = int(sys.stdin.readline().rstrip())
    
    if plays==0:
        break

    a = 0
    b = 0

    A = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    B = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    for i in range(plays):
        if abs(A[i]-B[i]) == 1:
            if A[i] > B[i]:
                if A[i] == 2:
                    b += 6
                else:
                    b += A[i] + B[i]
            else:  
                if B[i] == 2:
                    a += 6
                else:
                    a += A[i] + B[i]
        elif A[i] < B[i]:
            b += B[i]
        elif A[i] > B[i]:
            a += A[i]

    print("A has {} points. B has {} points.\n".format(a, b))