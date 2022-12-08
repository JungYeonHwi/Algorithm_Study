arr = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
N = int(input()) - 1
k = N // 14
if N % 14 in [3, 7, 11] :
    if k >= 4 : print(f"tu+ru*{k+1}")
    else : print("turu" + "ru" * k)    
elif N % 14 in [2, 6, 10] :
    if k >= 3 : print(f"tu+ru*{k+2}")
    else : print("tururu"+"ru"*k)    
else :
    print(arr[N % 14])