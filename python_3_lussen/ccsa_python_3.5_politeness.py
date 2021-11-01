n = int(input())
politeness = 0

for i in range(1, (n)):
  sum = 0
  for j in range(i, (n)):
    sum+= j
    if sum > n:
      break
    elif sum == n:
      politeness+=1
      break
    

print(politeness)  

    