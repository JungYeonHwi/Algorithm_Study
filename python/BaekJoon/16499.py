n = int(input())
 
arr = []

for _ in range(n):
    word = sorted(list(input()))
    word = ''.join(word)	
    if word not in arr:	
        arr.append(word)	
 
print(len(arr))