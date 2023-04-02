A, B, K = map(int, input().split())
print((A//K)*(B//K) - max(0, A//K-2)*max(0, B//K-2))