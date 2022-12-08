N, k = map(int, input().split())

List = list(map(int, input().split()))
List.sort()
List.reverse()

print(List[k-1])
