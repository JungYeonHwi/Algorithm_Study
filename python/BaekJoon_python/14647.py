n, m = map(int, input().split())
board = []

rowCntArr, columnCntArr = [], []

for i in range(n) : 
    arr = list(map(str, input().split()))
    board.append(arr)
    rowCnt = 0
    
    for a in arr : 
        rowCnt += a.count("9")
    rowCntArr.append(rowCnt)
    
for i in range(m) : 
    columnCnt = 0
    for j in range(n) :
        columnCnt += board[j][i].count("9")
    columnCntArr.append(columnCnt)
    
print(sum(rowCntArr) - max((max(rowCntArr), max(columnCntArr))))