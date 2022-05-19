n = int(input())
card = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

card.sort()

def Search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if array[mid] == target : return mid
        elif array[mid] > target : end = mid - 1
        else : start = mid + 1
        
    return None


for i in range(m) :
    if Search(card, check[i], 0, n - 1) is not None : print(1, end=' ')
    else : print(0, end=' ')