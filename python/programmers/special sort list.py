from itertools import chain
from collections import defaultdict

def solution(numlist, n):
    answer = []
    big = {}
    small ={}
    
    for i in numlist : 
        if i > n : 
            big[abs(n-i)] = i
        if i < n : 
            small[abs(n-i)] = i
        if i == n : answer.append(i)
        
    sortedBigList = sorted(big.items())
    sortedSmallList = sorted(small.items())
    bigSorted = dict(sortedBigList)
    smallSorted = dict(sortedSmallList)
    
    merge = defaultdict(list)

    for k, v in chain(bigSorted.items(), smallSorted.items()):
        merge[k].append(v)
        
    sortedMergeList = sorted(merge.items())
    mergeSorted = dict(sortedMergeList)

    for k, v in mergeSorted.items() :
        for i in v : answer.append(i)
            
    return answer