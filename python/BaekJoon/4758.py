wr = [4.5, 150, 200]
l = [6.0, 300, 500]
q = [5.0, 200, 300]

while 1 : 
    i, j, k = map(float, input().split())
    
    if i == j == k == 0 : break
    
    chk = 0
    
    if i <= wr[0] and j >= wr[1] and k >= wr[2] : 
        print("Wide Receiver", end=" ")
        chk = 1
    if i <= l[0] and j >= l[1] and k >= l[2] : 
        print("Lineman", end=" ")
        chk = 1
    if i <= q[0] and j >= q[1] and k >= q[2] : 
        print("Quarterback", end=" ")
        chk = 1
        
    if chk != 1 : print("No positions", end="")
    print()