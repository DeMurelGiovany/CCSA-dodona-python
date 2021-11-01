respiration = input()
pulse = int(input()) #heartbeats per minute#
activity = input()
appearance = input()
reflex = input()

pointsTotal = 0;
output = ""

if "weak" == respiration:
  pointsTotal+=1
elif "strong cry" == respiration:
  pointsTotal+=2
elif "absent" != respiration:
  output = "invalid input"
  
if pulse < 100 and pulse >0:
  pointsTotal+=1
elif pulse >= 100:
  pointsTotal+=2
elif pulse < 0:
  output = "invalid input"

if  activity == "some flexion":
  pointsTotal+=1
elif activity == "resist extension":
  pointsTotal+=2
elif activity !="none":
  output = "invalid input"

if appearance == "extremities": 
  pointsTotal+=1
elif appearance == "pink":
  pointsTotal+=2
elif  appearance not in ["blue", "pale"]:
  output = "invalid input"

if  reflex == "grimace":
  pointsTotal+=1
elif reflex == "cry or pull away":
  pointsTotal+=2
elif reflex != "no response":
  output = "invalid input"


if output != "invalid input":
     if pointsTotal < 4: 
      output = "alarm" 
     else: 
       output = pointsTotal

print(output)

     
      







""" ap = {
  "blue": 0,
  "weak": 0,
  "extremities": 1,
  "pink": 2
}
pu = {
  "0": 0,
  "100": 1,
  ""
}
gr = {

}
ac = {

}
re = {
 
} """

