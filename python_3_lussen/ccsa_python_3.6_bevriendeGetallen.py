a = int(input())
b = int(input())

totaalA = 0
totaalB = 0

for i in range(1, a):
  if a % i == 0:
    totaalA += i
for j in range(1, b):
  if b % j == 0:
    totaalB += j

if totaalA == b and totaalB == a:
  print(a,"en",b,"zijn bevriende getallen")
else:
  print(a,"en",b,"zijn geen bevriende getallen")
  