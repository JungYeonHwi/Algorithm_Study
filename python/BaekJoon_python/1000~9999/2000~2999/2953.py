List = []

A = list(map(int, input().split()))
List.append(sum(A))
B = list(map(int, input().split()))
List.append(sum(B))
C = list(map(int, input().split()))
List.append(sum(C))
D = list(map(int, input().split()))
List.append(sum(D))
E = list(map(int, input().split()))
List.append(sum(E))

m = max(List)
print(List.index(m)+1, m)