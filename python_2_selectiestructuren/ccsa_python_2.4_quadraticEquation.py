import math
a = float(input())
b = float(input())
c = float(input())

D = b**2-4*a*c

if D < 0:
  print("no roots")
elif D == 0:
  print(f"one root\n",-(b/(2*a)))
elif D > 0:
  root1 = (-b+math.sqrt(D))/(2*a)
  root2 = (-b-math.sqrt(D))/(2*a)
  if root1 < root2:
    print("two roots\n",root1,"\n",root2)
  else:
    print("two roots\n",root2,"\n",root1)