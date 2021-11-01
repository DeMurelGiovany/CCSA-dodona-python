coverPrice = 24.95
discount = 40
priceAfterDiscount = coverPrice*((100-discount)/100)
orderAmount = 60
shipping = 3+((orderAmount-1)*0.75)
#print(price)
#print(orderAmount)
#print(shipping)
print(priceAfterDiscount*orderAmount+shipping)