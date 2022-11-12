import sys
import re

whole = sys.stdin.readlines()
    
for code in whole :
    while 1 :
        code = re.sub(r'BUG', '', code)
        
        if 'BUG' not in code:
            break
    
    print(code, end='')