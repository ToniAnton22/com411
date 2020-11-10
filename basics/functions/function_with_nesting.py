# Creating a program with simple functions and nesting

def identify():
  sight = str(input("Tell us what do you see: "))
  print(sight)

  if sight == 'a large boulder':
    print("It's time to run!")

  else:
    print("We will be fine.")

identify()
