gesture1 = input()
gesture2 = input()

scissorsBeats = ['paper', 'lizard']
paperBeats = ['rock', 'Spock']
rockBeats = ['scissors', 'lizard']
lizardBeats = ['Spock', 'paper']
spockBeats = ['scissors', 'rock']

if gesture1 == gesture2:
    print('draw')
elif gesture1 == 'scissors':
   print("player1 wins") if gesture2 in scissorsBeats else print("player2 wins")
elif gesture1 == 'paper':
  print("player1 wins") if gesture2 in paperBeats  else print("player2 wins")
elif gesture1 == 'rock':
  print("player1 wins") if gesture2 in rockBeats  else print("player2 wins")
elif gesture1 == 'lizard':
  print("player1 wins") if gesture2 in lizardBeats  else print("player2 wins")
elif gesture1 == 'Spock':
  print("player1 wins") if gesture2 in spockBeats  else print("player2 wins")