t = int(input())

for i in range(1, t + 1) :
  gan = list(map(int, input().split()))
  sau = list(map(int, input().split()))

  ganScore = gan[0] + gan[1] * 2 + gan[2] * 3 + gan[3] * 3  + gan[4] * 4 + gan[5] * 10
  sauScore = sau[0] + sau[1] * 2 + sau[2] * 2 + sau[3] * 2 + sau[4] * 3 + sau[5] * 5 + sau[6] * 10

  if ganScore > sauScore : print(f"Battle {i}: Good triumphs over Evil")
  elif ganScore < sauScore : print(f"Battle {i}: Evil eradicates all trace of Good")
  else : print(f"Battle {i}: No victor on this battle field")