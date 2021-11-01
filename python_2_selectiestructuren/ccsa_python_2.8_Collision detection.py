sq1_x1 = int(input())
sq1_y1 = int(input())
sq1_x2 = int(input())
sq1_y2 = int(input())

sq2_x1 = int(input())
sq2_y1 = int(input())
sq2_x2 = int(input())
sq2_y2 = int(input())

# if  ( sq1_x1 > sq2_x1 and sq1_x1 < sq2_x2 ) or ( sq1_y1 > sq2_y1 and sq1_y1 < sq2_y2 ):
#   print("collision")
# else:
#   print("no collision")

if  ( (sq2_x1 >= sq1_x2 and sq2_y1 >= sq2_y2) or (sq2_x2 <= sq1_x1 and sq2_y2 <= sq1_y1)) :
  print("no collision")
else:
  print("collision")

