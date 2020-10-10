# creating the variables to help beep find his batteries

direction = input("Where should I look?")

if direction  == 'in the bedroom':
  location = input("Where in the bedroom should I look?")

  if location == 'under the bed':
    print("Found some shoes but no battery.")
  else:
    print("Found a mess but no battery.")

elif direction == 'in the bathroom':
  location = input("Where in the bathroom should I look?")

  if location == 'in the bathtub':
    print("Found a rubber duck but no battery.")

  else:
    print("Found a wet surface but no battery.")

elif direction == 'in the lab':
  location = input("Where in the lab should I look?")

  if location == 'on the table':
    print("YES! I found my battery!")

  else:
    print("Found some tools but no battery.")

else:
  print("I do now know where that is but I will keep looking.")