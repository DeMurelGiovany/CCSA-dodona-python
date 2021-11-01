firstWeighing = input()
secondWeighing = input()

coins = [
"coin #1", 
"coin #2",
"coin #3",
"coin #4", 
"coin #5", 
"coin #6", 
"coin #7", 
"coin #8", 
"coin #9"
]

group1 = [coins[0], coins[1], coins[2]]
group2 = [coins[3], coins[4], coins[5]]
group3 = [coins[6], coins[7], coins[8]]

if firstWeighing == "left":
  leftover = group2
elif firstWeighing == "right":
  leftover = group1
else:
  leftover = group3

if secondWeighing == "left":
  print(leftover[1]+" is counterfeit")
elif secondWeighing == "right":
  print(leftover[0]+" is counterfeit")
else:
  print(leftover[2]+" is counterfeit")
