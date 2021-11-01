n = int(input())
k = 0
for i in range (0, n):
  for j in range (0, i+1):
    k+=1
    print(k, end = "")
  print()
  k=0
