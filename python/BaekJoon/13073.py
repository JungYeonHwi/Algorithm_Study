for _ in range(int(input())):
    N = int(input())
    s1 = N*(N+1)//2
    s2 = int((N*2)*(N/2))
    s3 = int((N*2+2)*(N/2))
    print(s1, s2, s3)