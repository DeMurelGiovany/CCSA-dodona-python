import math
#from decimal import *
#getcontext().prec = 11
sum = 0
n = 0
for i in range(1, 101):
  sum += 1 / ( i ** 2 )
  if ( n == 0 or sum < n ) and abs(sum-((math.pi)**2)/6) <= 1/100:
    n = i
print('{0:.11f}'.format(sum))
print(n)
#print(Decimal(str(sum)))
#print(str( '%.11f' ))