#Adding elif to give everything life

paintDirection = input("Towards which direction should I paint (up, down, left or right)? ")

if paintDirection == 'up':
  print("I am painting in the upwards direction.")
elif paintDirection == 'down':
  print("Downwards it is!")
elif paintDirection == 'right':
  print("Sliiiide to the right")
elif paintDirection == 'left':
  print("Sliiiide to the left")
else:
  print("We are only 3d :( !")