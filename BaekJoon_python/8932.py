def track(A, B, C, P ) : return int(A * (B - P) ** C)

def field(A, B, C, P) : return int(A * (P - B) ** C)

for _ in range(int(input())) :
    arr = list(map(int, input().split()))
    answer = track(9.23076, 26.7, 1.835, arr[0]) + field(1.84523, 75, 1.348, arr[1]) + field(56.0211, 1.5, 1.05, arr[2]) + track(4.99087, 42.5, 1.81, arr[3]) + field(0.188807, 210, 1.41, arr[4]) + field(15.9803, 3.8, 1.04, arr[5]) + track(0.11193, 254, 1.88, arr[6])
    print(answer)