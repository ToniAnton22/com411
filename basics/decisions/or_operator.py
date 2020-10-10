# Adventuring program commencing 

typeadv = input("What type of adventure do you want short/scary or safe/long): ")

#The or function works by taking 2 conditions
# and only be one being required to be true in order
# to run the program
if typeadv == 'short' or typeadv == 'scary':
  print("Entering the dark forest.")
elif typeadv == 'long' or typeadv == 'safe':
  print("Taking the safe router!")
else:
  print("Not sure which route to take.")

