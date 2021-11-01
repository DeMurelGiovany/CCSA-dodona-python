# def hallo(naam, roepen=False):
#     if roepen:
#         return f"HALLO, {naam.upper()}!"
#     else:
#         return f"Hallo, {naam}."

# print(hallo("wereld"))
# print(hallo("wereld", True))

def maximum_exposure(value):
  if value < 80:
    return -1.0  
  else:
    dbOver80 = value - 80
    exposure = 28800.0

    while value >= 83:
      exposure = exposure / 2
      value -= 3

    return exposure

  print(maximum_exposure)
