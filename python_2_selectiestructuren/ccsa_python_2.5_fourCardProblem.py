face = input()
if face == "value":
  number = int(input())
else:
   color = input() 
answer = input()

if face == "value":
  if number % 2 == 0 and answer == "yes":
    print("Correct: cards with value ",number,"must be turned.")
  elif number % 2 == 0 and answer == "no":
    print("Wrong: cards with value",number,"must be turned.")
  
  if number % 2 != 0 and answer == "yes":
    print("Wrong: cards with value",number,"must not be turned.")
  elif number % 2 != 0 and answer == "no":
    print("Correct: cards with value",number,"must not be turned.")
else:   
  if color == "red" and answer == "yes":
    print("Wrong: cards with color "+color+" must not be turned.")
  elif color == "red" and answer == "no":
    print("Correct: cards with color "+color+" must not be turned.")
  elif answer =="yes":
    print("Correct: cards with color "+color+" must be turned.")
  else:
    print("Wrong: cards with color "+color+" must be turned.")
