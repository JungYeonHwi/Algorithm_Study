t = int(input())

for _ in range(t) : 
    A, B = input().split()
    a = list(map(str, A))
    b = list(map(str, B))
    a.sort()
    b.sort()
    
    if a == b : print(A, '&', B, 'are anagrams.')
    else : print(A, '&', B, 'are NOT anagrams.')