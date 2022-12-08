List1 = list(map(int, input().split()))
S = sum(List1)
List2 = list(map(int, input().split()))
T = sum(List2)

if (S >= T) : print(S)
else : print(T)