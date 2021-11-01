apples = int(input())

crateCapacity = 20
palletCapacity = 35

fullCrates = apples//crateCapacity
remainder = apples%crateCapacity

fullPallets = fullCrates//palletCapacity
leftoverFullCrates = fullCrates%palletCapacity

print(fullPallets)
print(leftoverFullCrates)
#print(fullCrates)
print(remainder)


