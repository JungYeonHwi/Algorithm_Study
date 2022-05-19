n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
    
AS = set(A)
BS = set(B)

AB = AS - BS
BA = BS - AS

print(len(AB) + len(BA))