import sys
input = sys.stdin.readline

for _ in range(int(input())) : 
    n = int(input())
    nums1 = set(map(int, input().split()))
    m = int(input())
    nums2 = set(map(int, input().split()))
    
    for i in nums2 : 
        if i in nums1 : print(1)
        else : print(0)