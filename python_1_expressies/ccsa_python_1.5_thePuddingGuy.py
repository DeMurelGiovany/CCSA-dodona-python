aantalItems = int(input())
kostPerItem = float(input())
aantalBarcodesVoorCoupon = int(input())
FFMilesPerCoupon = int(input())
print("Phillips spent $"+ str(aantalItems*kostPerItem) +" for "+ str(int(aantalItems/aantalBarcodesVoorCoupon)*FFMilesPerCoupon) +" frequent-flyer miles.")