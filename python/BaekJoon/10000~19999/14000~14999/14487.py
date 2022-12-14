n = int(input())
List = list(map(int, input().split( )))
m = max(List)

print(sum(List) - m)