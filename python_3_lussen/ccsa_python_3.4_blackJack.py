totaal = 0
cont = True
while cont == True:
  kaart = int(input())
  totaal+= kaart
  if totaal > 21:
    print("Verbrand ("+str(totaal)+")")
    break
  if totaal == 21:
    print("Gewonnen!")
    break
  if kaart == 0:
    print("Voorzichtig gespeeld ("+str(totaal)+")")
    break