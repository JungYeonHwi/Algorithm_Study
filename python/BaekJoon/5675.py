import sys
for i in sys.stdin : print("NY"[int(i)%6==0])