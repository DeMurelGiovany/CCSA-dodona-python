redAndWhite = int(input()) 
whiteAndBlue = int(input())
operator = input()

blue = 0
white = 0
red = 0

redBlueDifference = redAndWhite - whiteAndBlue

if operator == ">":
  for i in range(2, redAndWhite + whiteAndBlue - redBlueDifference - 2, 2):
    blue += 1
elif operator == "<":
  for i in range(2, whiteAndBlue - redBlueDifference, 2):
    blue+= 1

white = whiteAndBlue - blue    
red = redAndWhite - white
print(blue)
print(white)
print(red)