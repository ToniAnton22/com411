
distance = int()
def cross_bridge(distance):

  counter = 0

  while counter < distance:
    print("Crossed Step")
    counter += 1

  if distance > 6:

   print("The bridge is collapsing!")

  else:
    print("We must keep going!")
    
  
cross_bridge(3)
cross_bridge(6)
